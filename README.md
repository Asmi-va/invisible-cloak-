# invisible-cloak-
---

# Invisibility Cloak with Automatic Color Detection

This project replicates the famous invisibility cloak effect using computer vision and OpenCV. The application captures a live video feed, detects the cloak's color automatically, and replaces it with a pre-captured background, creating an invisibility illusion.

## Features
- **Automatic Color Detection**: No need to manually set the color of the cloak. The system detects the dominant color of the cloak region and adjusts its detection accordingly.
- **Real-time Processing**: The program captures live video, detects the cloak color, and applies the effect in real-time.
- **Background Replacement**: The cloak area in the video is replaced by a static background that was captured at the beginning of the program.

## How It Works
1. The system captures the background for a few seconds before the invisibility effect starts.
2. The dominant color of the cloak is automatically detected from a region of interest in the video feed.
3. Pixels matching the cloak color are replaced with the captured background, making the cloak "invisible" while the rest of the scene remains visible.
4. The program writes the output to a video file (`output_auto_detect.avi`) and displays the "invisibility" effect in real-time.

## Requirements
- Python 3.x
- OpenCV (cv2)
- NumPy

Install the dependencies using the following command:

```bash
pip install opencv-python numpy
```

## Usage

1. Clone this repository or download the source code files.

2. Run the Python script:

   ```bash
   python invisibility_cloak.py
   ```

3. When the script runs:
   - The system waits for a 3-second countdown to give you time to position the camera.
   - The system captures the background for 60 frames.
   - After the countdown, wear your cloak, and the system will automatically detect the cloak color and replace it with the pre-captured background.

4. To stop the script, press the **`q`** key.

## Code Breakdown

- **`get_dominant_color()`**: Automatically detects the most dominant color in a specific region of the video feed, which helps detect the cloak's color.
- **`mask1`** and **`mask2`**: Used to isolate the cloak by detecting pixels that match the cloak's color and apply the invisibility effect.
- **Real-time Video Processing**: Each frame is processed to replace the cloak area with the captured background and combine the results.

## Output

- The processed video feed is displayed in real-time in a window titled `Magic Cloak!`.
- A video recording of the invisibility effect is saved as `output_auto_detect.avi`.

## Example Output

The person wearing the cloak becomes invisible, with the cloak's area being replaced by the pre-captured background.

## Future Improvements

- Implement gesture detection for additional effects.
- Improve robustness in varying lighting conditions.
- Add additional color detection for different colored cloaks.

## License
This project is open-source and available under the MIT License.
