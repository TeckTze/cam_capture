import cv2
import time

# Function to generate a unique filename based on time
def get_new_filename():
    return time.strftime("%Y-%m-%d_%H-%M-%S") + ".mp4"

def main():
    # Initialize parameters
    frame_rate = 5 # fps
    video_duration = 10
    frame_interval = 1/ frame_rate # Time between frames

    # Open the webcam
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("Error: Could not open device")
        exit()

    # Define codec and resolution (adjust as needed)
    fourcc =  cv2.VideoWriter_fourcc(*'mp4v') # H.264 codec for .mp4
    frame_width, frame_height = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)), int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

    # Start the video writer for the first file
    out = cv2.VideoWriter(get_new_filename(), fourcc, frame_rate, (frame_width, frame_height))

    start_time = time.time()
    video_start_time = start_time

    # Simulate video capture loop (replace with actual capture code)
    while True:
        current_time = time.time()

        if current_time - video_start_time >= video_duration:
            print("Releasing")
            # Release the current video file
            out.release()

            # Create a new video file
            out = cv2.VideoWriter(get_new_filename(), fourcc, frame_rate, (frame_width, frame_height))

            # Reset the start tiem for the new video
            video_start_time = current_time

        ret, frame = cap.read()

        if not ret:
            print("Failed to capture frame")
            break

        out.write(frame)
        time.sleep(frame_interval)

    # Release everything when the job is done
    cap.release()
    out.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()