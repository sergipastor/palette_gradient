# palette gradient

palette gradient generates a gradient image using a color palette consisting of 2 to 4 colors provided as input. The resulting image smoothly transitions between the specified colors, creating a visually pleasing gradient effect.

| Two colors    | Three colors   | Four colours  |
|     :---:     |      :---:     |     :---:     |
| ![uhaha](examples/example1.png)   | ![uhaha](examples/example2.png)     | ![uhaha](examples/example3.png)    |


## Requirements

To run this program, you need the following:

- **Python 3.x**

- **Python Dependencies:** You can easily install the required Python libraries using `pip` and the provided `requirements.txt` file.

   ```shell
   pip3 install -r requirements.txt
   ```

## Usage

```shell
python3 palette_gradient.py -o ./example3.png --colors '#000000' '#7c4699' '#bdab39' '#4bbd39' --distribution top-bottom
```

### Arguments
- **Output filename** (`-o/--output_filename`) [_required_]
- **Colors** (`-c/--colors`) [_optional_]: Hexadecimal values of the colors to be used in the resulting image.
- **Distribution** (`-d/--distribution`) [_optional_]: Distribution of the colors provided in the resulting image. 
    - `top-bottom`: first colors at the top, last colors at the bottom.
    - `bottom-top`: first colors at the bottom, last colors at the top.
    - `right-left`: first colors on the right side, last colors on the left side.
    - `left-right`: first colors on the left side, last colors on the right side.