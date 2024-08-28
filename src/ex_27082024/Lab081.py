def add_before_ui_after_ui(func):
    def wrapper():
        print("Before running the UI Testing")
        print("Open the browser")
        func()
        print("After running the UI Testing")
        print("Quit the browser")
        func()

    return wrapper()


@add_before_ui_after_ui
def test_ui():
    print("I will test the UI")
