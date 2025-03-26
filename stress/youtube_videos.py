import random

def get_meditation_video():
    meditation_videos = [
        "https://www.youtube.com/watch?v=inpok4MKVLM",  # 10-minute meditation
        "https://www.youtube.com/watch?v=O-6f5wQXSu8",  # Deep breathing exercise
        "https://www.youtube.com/watch?v=ZToicYcHIOU"   # Guided meditation
    ]
    return random.choice(meditation_videos)

def get_dance_video():
    dance_videos = [
        "https://youtu.be/9DhwZqNJkIU?si=WmMQ3Z-fZcy6KlDR",  # Zumba dance workout
        "https://youtu.be/rvu7iNIrNa8?si=yqXDQYqdn-8jao1b",  # Fun dance workout
        "https://youtu.be/5X3vxcAO2W8?si=oIPS39MlUoz2Mjck"   # Cardio dance
    ]
    return random.choice(dance_videos)

def get_music_video():
    music_videos = [
        "https://youtu.be/lFcSrYw-ARY?si=4KiqVpJyVaEEcEK_",  # Ed Sheeran - Perfect
        "https://youtu.be/xRcWlA1I9z0?si=XurvDakfgPB9WSii",  # James Arthur - Say You Won't Let Go
        "https://youtu.be/PNiLq-cZUBU?si=gQ7SWEsaE-Vk29of"   # Ed Sheeran - Shape of You
    ]
    return random.choice(music_videos)