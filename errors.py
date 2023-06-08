def Error(error, app):

    if error == "id":
        app.send_sticker(
            chat_id="me",
            sticker=open("DATA/sticker02.webp", "rb")
        )
        app.send_message(
            chat_id="me",
            text="""
There is a problem with the numeric ID of the target channel

Please check the ID
Enter the channel ID according to the instructions in the `HELP.txt` file
            """
        )

    if error == "channel":
        app.send_sticker(
            chat_id="me",
            sticker=open("DATA/sticker02.webp", "rb")
        )
        app.send_message(
            chat_id="me",
            text="""
There was a problem creating the channel, please try again later
            """
        )

    if error == "files":
        app.send_message(
            chat_id="me",
            text="""
Part of the set of program files has a problem, it may be damaged or deleted
Run `Debug.py` to fix
            """
        )
