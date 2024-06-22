const formatTime = (seconds) => {
    const minutes = Math.floor(seconds / 60);
    const secs = Math.floor(seconds % 60);
    return `${minutes}:${secs < 10 ? '0' : ''}${secs}`;
}

document.addEventListener('DOMContentLoaded', () => {
    const audio = document.getElementById('audio');
    const playPauseBtn = document.getElementById('play-pause');
    const progressBar = document.getElementById('progress-bar');
    const curTimeAudioSpan = document.getElementById("cur-time-audio-player")
    const maxTimeAudioSpan = document.getElementById("max-time-audio-player")
    maxTimeAudioSpan.textContent = formatTime(audio.duration);

    playPauseBtn.addEventListener('click', () => {
        if (audio.paused) {
            audio.play();
            playPauseBtn.textContent = '◼';
        } else {
            audio.pause();
            playPauseBtn.textContent = '▶';
        }
    });
    
    
    audio.addEventListener('timeupdate', () => {
        const progress = (audio.currentTime / audio.duration) * 100;
        progressBar.value = progress;
        curTimeAudioSpan.textContent = formatTime(audio.currentTime);
       
    });


    progressBar.addEventListener('click', (e) => {
        const rect = progressBar.getBoundingClientRect();
        const offsetX = e.clientX - rect.left;
        const newTime = (offsetX / rect.width) * audio.duration;
        audio.currentTime = newTime;
    });
});