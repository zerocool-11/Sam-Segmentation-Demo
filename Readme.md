# SAM2.1 and FastSAM Example Script

This script demonstrates the use of the **Segment Anything Model (SAM)** and **FastSAM** for image segmentation tasks. The script allows users to interactively test various prompts like bounding boxes, single points, multiple points, and negative points.

## Features

- **Bounding Box Prompt**: Segment using a bounding box.
- **Single Point Prompt**: Segment using a single point.
- **Multiple Points Prompt**: Segment using multiple points.
- **Negative Points Prompt**: Segment with positive and negative points.
- **Open-Source Flexibility**: Choose between SAM or FastSAM models.

## System Requirements

### Hardware
- **CPU**: Minimum 4 cores.
- **GPU**: NVIDIA GPU with CUDA support (recommended for faster processing).
- **Memory**: Minimum 8GB RAM.

### Software
- **Python**: Version 3.8 or higher.
- **Dependencies**:
  - `ultralytics`
  - `opencv-python`

Install dependencies with:

```bash
pip install ultralytics opencv-python
```

## Usage

1. Clone this repository:
   ```bash
   git clone https://github.com/your-repo/sam-example.git
   cd sam-example
   ```

2. Place your image file in the same directory as the script and rename it to `nature.jpg`. Alternatively, update the script with your image path.

3. Run the script:
   ```bash
   python sam_script.py
   ```

4. Follow the prompts in the terminal to select a segmentation method:
   - `1`: Bounding Box
   - `2`: Single Point
   - `3`: Multiple Points
   - `4`: Multiple Points Prompt per Object
   - `5`: Negative Points Prompt

## Models

You can experiment with different models:
- **SAM (default)**: `sam2.1_s.pt`
- **FastSAM**: Uncomment the relevant line in the script to use `FastSAM-s.pt` or `FastSAM-x.pt`.

Download models from the [Ultralytics Model Hub](https://ultralytics.com).

## Examples


### Single Point
- Input: A single point marking the object to segment.
- Example Output:
  ![Single Point Example](images/single_point.png)


