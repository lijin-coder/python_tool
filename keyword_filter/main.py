import display


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print ('hello')
    try:
        app = display.create_qt_application()
        window = display.display_main()

        display.exit_qt_application(app.exec_())

    except Exception as rt:
        print (rt)
        print (rt.__traceback__.tb_lineno)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
