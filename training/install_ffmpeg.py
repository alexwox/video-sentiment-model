import subprocess
import sys
import os

def install_ffmpeg():
    print("Starting Ffmpeg installation...")
    
    subprocess.check_call([sys.executable, "-m", "pip", "install", "--upgrade", "pip"])
    subprocess.check_call([sys.executable, "-m", "pip", "install", "--upgrade", "setuptools"])
    
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "ffmpeg-python"])
        print("Installed ffmpeg python successfully")
        
    except subprocess.CalledProcessError as e:
        print("Failed to install ffmpeg-python via pip")
        
    try:
        print("Downloading FFmpeg...")
        subprocess.check_call(["wget", "https://johnvansickle.com/ffmpeg/releases/ffmpeg-release-amd64-static.tar.xz",
                               "-O", "/tmp/ffmpeg.tar.xz"])
        
        if not os.path.exists("/tmp/ffmpeg.tar.xz"):
            raise FileNotFoundError("FFmpeg download failed - tar.xz file not found")
            
        print("Extracting FFmpeg...")
        subprocess.check_call(["tar", "-xf", "/tmp/ffmpeg.tar.xz", "-C", "/tmp"])
        print("Running find command...")
        result = subprocess.run(["find", "/tmp", "-name", "ffmpeg", "-type", "f"],
                                capture_output=True,
                                text=True,
                                check=True
        )
        
        ffmpeg_path = result.stdout.strip()
        print(f"Found FFmpeg at: {ffmpeg_path}")
        if not ffmpeg_path:
            print(f"Find command stderr: {result.stderr}")
            raise ValueError("FFmpeg binary not found in extracted files")
            
        subprocess.check_call(["cp", ffmpeg_path, "/usr/local/bin/ffmpeg"])
        subprocess.check_call(["chmod", "+x", "/usr/local/bin/ffmpeg"])
        print("Installed static FFMPEG binary successfully")
        

    except Exception as e:
        print(f"Failed install static FFmpeg: {e}")
    
    try: 
        result = subprocess.run(["ffmpeg", "-version"], capture_output=True, text=True, check=True)
        print("FFmpeg version:")
        print(result.stdout)
        return True
    
    except (subprocess.CalledProcessError, FileNotFoundError) as e:
        print("FFmpeg install verification failed")
        print(f"Error: {str(e)}")
        return False
        

