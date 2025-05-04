import tensorflow as tf

class ImgProcessor:
    def __init__(self, filePath):
        self.filePath = filePath
        self.data = None

    def loadImageData(self):
        self.data = tf.io.read_file(self.filePath)

    def initial_processing(self):
        image = tf.image.decode_jpeg(self.data, channels=3)
        print(f"Shape (Height, Width, Channels): {image.shape}")
        print(f"Image Height: {image.shape[0]} pixels")
        print(f"Image Width: {image.shape[1]} pixels")
        print(f"Number of Channels: {image.shape[2]}")
        print(f"Image Data Type: {image.dtype}")

def main():
    imgPath = "example.jpg"
    imgProcessor = ImgProcessor(imgPath)
    imgProcessor.loadImageData()
    imgProcessor.initial_processing()

if __name__ == "__main__":
    main()