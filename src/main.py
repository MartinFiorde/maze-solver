from src.models.window import Window


def main():
    print("hello word")
    win = Window(800, 600)
    win.wait_for_close()


if __name__ == "__main__":
    main()
