import * as THREE from 'three';

// --- CONFIG & STATE ---
const state = {
    audioEnabled: false,
    videoEnabled: false,
    audioContext: null,
    analyser: null,
    dataArray: null,
    motionData: { x: 0, y: 0, intensity: 0 },
    lastFrame: null,
};

// --- THREE.JS SETUP ---
const scene = new THREE.Scene();
const camera = new THREE.PerspectiveCamera(75, window.innerWidth / window.innerHeight, 0.1, 1000);
const renderer = new THREE.WebGLRenderer({
    canvas: document.querySelector('#canvas3d'),
    antialias: true,
    alpha: true
});
renderer.setSize(window.innerWidth, window.innerHeight);
renderer.setPixelRatio(Math.min(window.devicePixelRatio, 2));

// --- OBJECTS ---
// 1. Neural Core
const coreGeometry = new THREE.IcosahedronGeometry(2, 2);
const coreMaterial = new THREE.MeshPhongMaterial({
    color: 0x00f2ff,
    wireframe: true,
    transparent: true,
    opacity: 0.8,
    emissive: 0x00f2ff,
    emissiveIntensity: 0.5
});
const core = new THREE.Mesh(coreGeometry, coreMaterial);
scene.add(core);

// 2. Particle Cloud
const particlesCount = 1500;
const positions = new Float32Array(particlesCount * 3);
for (let i = 0; i < particlesCount * 3; i++) {
    positions[i] = (Math.random() - 0.5) * 15;
}
const particlesGeometry = new THREE.BufferGeometry();
particlesGeometry.setAttribute('position', new THREE.BufferAttribute(positions, 3));
const particlesMaterial = new THREE.PointsMaterial({
    color: 0xffffff,
    size: 0.03,
    transparent: true,
    opacity: 0.5
});
const particles = new THREE.Points(particlesGeometry, particlesMaterial);
scene.add(particles);

// 3. Lights
const ambientLight = new THREE.AmbientLight(0x404040, 2);
scene.add(ambientLight);

const pointLight = new THREE.PointLight(0x00f2ff, 5, 20);
pointLight.position.set(2, 3, 4);
scene.add(pointLight);

camera.position.z = 10;

// 4. 3D Image Carousel
const carouselGroup = new THREE.Group();
scene.add(carouselGroup);

const textureLoader = new THREE.TextureLoader();
const imgPaths = [
    './assets/img1.png', './assets/img2.png', './assets/img3.png',
    './assets/img4.png', './assets/img5.png', './assets/img6.png'
];
const images = [];

imgPaths.forEach((path, i) => {
    const geometry = new THREE.PlaneGeometry(4, 2.5);
    const material = new THREE.MeshPhongMaterial({ 
        map: textureLoader.load(path),
        side: THREE.DoubleSide,
        transparent: true,
        opacity: 0.8,
        emissive: 0x00f2ff,
        emissiveIntensity: 0
    });
    const plane = new THREE.Mesh(geometry, material);
    
    // Position in a circle
    const angle = (i / imgPaths.length) * Math.PI * 2;
    const radius = 6;
    plane.position.x = Math.cos(angle) * radius;
    plane.position.z = Math.sin(angle) * radius;
    plane.lookAt(0, 0, 0); // Always face the center
    
    carouselGroup.add(plane);
    images.push(plane);
});

// --- AUDIO LOGIC ---
async function setupAudio() {
    try {
        const stream = await navigator.mediaDevices.getUserMedia({ audio: true });
        state.audioContext = new (window.AudioContext || window.webkitAudioContext)();
        
        // Ensure AudioContext is running
        if (state.audioContext.state === 'suspended') {
            await state.audioContext.resume();
        }

        const source = state.audioContext.createMediaStreamSource(stream);
        state.analyser = state.audioContext.createAnalyser();
        state.analyser.fftSize = 256;
        state.analyser.smoothingTimeConstant = 0.8; // Smooth animations
        source.connect(state.analyser);
        
        const bufferLength = state.analyser.frequencyBinCount;
        state.dataArray = new Uint8Array(bufferLength);
        
        const audioStatus = document.getElementById('audio-status');
        audioStatus.innerText = 'ACTIVE';
        audioStatus.style.color = '#00f2ff';
        state.audioEnabled = true;
        console.log("Audio setup successful");
    } catch (err) {
        console.error("Audio error:", err);
        document.getElementById('audio-status').innerText = 'ERROR (Check Mic)';
        document.getElementById('audio-status').style.color = '#ff4444';
    }
}

// --- MOTION LOGIC (Webcam) ---
const video = document.getElementById('webcam');
const motionCanvas = document.createElement('canvas');
const motionCtx = motionCanvas.getContext('2d');

async function setupVideo() {
    try {
        const stream = await navigator.mediaDevices.getUserMedia({ video: true });
        video.srcObject = stream;
        video.onloadedmetadata = () => {
            motionCanvas.width = 48; 
            motionCanvas.height = 36;
            video.classList.remove('hidden');
            state.videoEnabled = true;
            const motionStatus = document.getElementById('motion-status');
            motionStatus.innerText = 'ACTIVE';
            motionStatus.style.color = '#00f2ff';
        };
    } catch (err) {
        console.warn("Video access denied or not available:", err);
        const motionStatus = document.getElementById('motion-status');
        motionStatus.innerText = 'DISABLED (No Cam)';
        motionStatus.style.color = '#ff9900';
    }
}

function detectMotion() {
    if (!state.videoEnabled) return;

    motionCtx.drawImage(video, 0, 0, motionCanvas.width, motionCanvas.height);
    const currentFrame = motionCtx.getImageData(0, 0, motionCanvas.width, motionCanvas.height);

    if (state.lastFrame) {
        let totalDiff = 0;
        let centerX = 0;
        let centerY = 0;
        let diffCount = 0;

        for (let i = 0; i < currentFrame.data.length; i += 4) {
            const diff = Math.abs(currentFrame.data[i] - state.lastFrame.data[i]);
            if (diff > 40) { // Threshold
                const x = (i / 4) % motionCanvas.width;
                const y = Math.floor((i / 4) / motionCanvas.width);
                centerX += x;
                centerY += y;
                totalDiff += diff;
                diffCount++;
            }
        }

        if (diffCount > 10) {
            // Normalize coordinates to -1 to 1
            state.motionData.x = (centerX / diffCount / motionCanvas.width) * 2 - 1;
            state.motionData.y = (centerY / diffCount / motionCanvas.height) * 2 - 1;
            state.motionData.intensity = totalDiff / (motionCanvas.width * motionCanvas.height);
        }
    }
    state.lastFrame = currentFrame;
}

// --- MAIN LOOP ---
function animate() {
    requestAnimationFrame(animate);

    // 1. Update from Audio
    if (state.audioEnabled && state.analyser) {
        state.analyser.getByteFrequencyData(state.dataArray);
        
        let sum = 0;
        let max = 0;
        for (let i = 0; i < state.dataArray.length; i++) {
            sum += state.dataArray[i];
            if (state.dataArray[i] > max) max = state.dataArray[i];
        }
        const avg = sum / state.dataArray.length;
        
        // High sensitivity: use both average and peak (max)
        // This makes it react even to quiet talking
        const volumeScale = 1 + (avg / 40) + (max / 100);
        
        core.scale.set(volumeScale, volumeScale, volumeScale);
        core.material.emissiveIntensity = (avg / 20); 
        pointLight.intensity = (avg / 40) * 20;
        
        // Dynamic color based on audio spectrum
        const bass = state.dataArray[0] || 0;
        core.material.color.setHSL((180 + bass) / 360, 1, 0.5);
    }

    // 2. Update from Motion
    detectMotion();
    if (state.videoEnabled) {
        // Smoothly follow motion (lerp)
        const targetX = state.motionData.x * 2;
        const targetY = -state.motionData.y * 2;
        
        camera.position.x += (targetX - camera.position.x) * 0.05;
        camera.position.y += (targetY - camera.position.y) * 0.05;
        
        // Zoom in if high intensity motion (approaching)
        const targetZ = 8 - (state.motionData.intensity * 0.2);
        camera.position.z += (targetZ - camera.position.z) * 0.05;
        
        camera.lookAt(0, 0, 0);
    }

    // 3. Carousel Motion Control
    if (state.videoEnabled) {
        // Horizontal: Rotation
        const targetRotation = -state.motionData.x * Math.PI;
        carouselGroup.rotation.y += (targetRotation - carouselGroup.rotation.y) * 0.05;
        
        // Vertical: Height and Tilt
        const targetY = -state.motionData.y * 3;
        carouselGroup.position.y += (targetY - carouselGroup.position.y) * 0.05;
        
        const targetTilt = state.motionData.y * 0.5;
        carouselGroup.rotation.x += (targetTilt - carouselGroup.rotation.x) * 0.05;

        // SELECTION LOGIC: Highlight the one closest to camera
        let closestImg = null;
        let maxZ = -Infinity;

        images.forEach(img => {
            const worldPos = new THREE.Vector3();
            img.getWorldPosition(worldPos);
            
            // Check proximity to camera (larger Z is closer)
            if (worldPos.z > maxZ) {
                maxZ = worldPos.z;
                closestImg = img;
            }

            // Reset others
            img.scale.set(1, 1, 1);
            img.material.emissiveIntensity = 0;
            img.material.opacity = 0.6;
        });

        if (closestImg) {
            closestImg.scale.set(1.2, 1.2, 1.2);
            closestImg.material.emissiveIntensity = 0.5;
            closestImg.material.opacity = 1.0;
        }

    } else {
        carouselGroup.rotation.y += 0.002;
    }

    // 4. Constant rotation for core
    core.rotation.y += 0.005;
    core.rotation.x += 0.002;
    particles.rotation.y -= 0.001;

    renderer.render(scene, camera);
}

// --- INITIALIZATION ---
document.getElementById('startBtn').addEventListener('click', async () => {
    document.getElementById('overlay').classList.add('hidden');
    document.getElementById('status-bar').classList.remove('hidden');
    
    await setupAudio();
    await setupVideo();
    
    animate();
});

// Window Resize
window.addEventListener('resize', () => {
    camera.aspect = window.innerWidth / window.innerHeight;
    camera.updateProjectionMatrix();
    renderer.setSize(window.innerWidth, window.innerHeight);
});
