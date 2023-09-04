""" Main Chess Tournament program launcher"""

from controller.chess_controller import Controller


def main():
    """Main program
    """

    controller = Controller()
    controller.run()


if __name__ == "__main__":
    main()
