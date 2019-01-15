import subprocess
import threading


def start_transcode_pipeline(url, uuid):
    ffmpeg_thread = threading.Thread(target=run_ffmpeg, args=(url, uuid))
    ffmpeg_thread.start()


def run_ffmpeg(url, uuid):
    output_file = '{}.avi'.format(uuid)
    try:
        subprocess.run(
                ['ffmpeg', '-i', url, output_file],
                check=True, stderr=subprocess.STDOUT)
    except subprocess.CalledProcessError:
        print('Calling ffmpeg failed')
        return

    return output_file
