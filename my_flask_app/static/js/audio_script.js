const formatTime = (seconds) => {
    const minutes = Math.floor(seconds / 60);
    const secs = Math.floor(seconds % 60);
    return `${minutes}:${secs < 10 ? '0' : ''}${secs}`;
}

document.addEventListener('DOMContentLoaded', () => {
    const audioPlayers = document.querySelectorAll('.audio-player.box');

    audioPlayers.forEach((audioPlayer) => {
        const audio = audioPlayer.querySelector('audio');
        const playPauseBtn = audioPlayer.querySelector('.play-pause');
        const progressBar = audioPlayer.querySelector('progress');
        const curTimeAudioSpan = audioPlayer.querySelector(".cur-time-audio-player");
        const maxTimeAudioSpan = audioPlayer.querySelector(".max-time-audio-player");

        audio.addEventListener('loadedmetadata', () => {
            maxTimeAudioSpan.textContent = formatTime(audio.duration);
        });

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
});
