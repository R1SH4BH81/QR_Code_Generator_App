"""from __future__ import print_function
def spec():
    f =open ("12.spec", mode='r', encoding='utf-8')
    print(f.read())

    f.close()
    f1 = open("wm.txt", mode='r', encoding='utf-8')
    print(f1.read())

    f1.close()
def cr():

    from time import sleep
    # animation = ["10%", "20%", "30%", "40%", "50%", "60%", "70%", "80%", "90%", "100%"]
    animation = ["[■□□□□□□□□□]", "[■■□□□□□□□□]", "[■■■□□□□□□□]", "[■■■■□□□□□□]", "[■■■■■□□□□□]", "[■■■■■■□□□□]",
                 "[■■■■■■■□□□]", "[■■■■■■■■□□]", "[■■■■■■■■■□]", "[■■■■■■■■■■]"]

    for i in range(len(animation)):
        sleep(0.1)
        sys.stdout.write("\r" + animation[i % len(animation)])
        sys.stdout.flush()

    print("\n")
    string = "LOADING INFO...\n"

    for letter in string:
        sleep(0.6)  # In seconds
        sys.stdout.write(letter)
        sys.stdout.flush()

    string = "created by Rishabh Mishra\n Have a nice day :) "

    for letter in string:
        sleep(0.3)  # In seconds
        sys.stdout.write(letter)
        sys.stdout.flush()
    rst = input("restart? (y/n)")
    if rst == "y":
        restart()
        print("")
    elif rst == "n":

        print("Disconnecting  Console ...:")

        # animation = ["10%", "20%", "30%", "40%", "50%", "60%", "70%", "80%", "90%", "100%"]
        animation = ["[■□□□□□□□□□]", "[■■□□□□□□□□]", "[■■■□□□□□□□]", "[■■■■□□□□□□]", "[■■■■■□□□□□]", "[■■■■■■□□□□]",
                     "[■■■■■■■□□□]", "[■■■■■■■■□□]", "[■■■■■■■■■□]", "[■■■■■■■■■■]"]

        for i in range(len(animation)):
            sleep(0.02)
            sys.stdout.write("\r" + animation[i % len(animation)])
            sys.stdout.flush()

        print("\n")
        print("done...")


def restart():

    from time import sleep
    import sys
    string = "R1SH4BH\n"

    for letter in string:
        sleep(0.01)  # In seconds
        sys.stdout.write(letter)
        sys.stdout.flush()
    for i in range(21):
        sys.stdout.write('\r')
        # the exact output you're looking for:
        sys.stdout.write("[%-20s] %d%%" % ('ᴵ' * i, 5* i))
        sys.stdout.flush()
        sleep(0.05)





    from time import sleep
    # animation = ["10%", "20%", "30%", "40%", "50%", "60%", "70%", "80%", "90%", "100%"]
    animation = ["[■□□□□□□□□□]", "[■■□□□□□□□□]", "[■■■□□□□□□□]", "[■■■■□□□□□□]", "[■■■■■□□□□□]", "[■■■■■■□□□□]",
                 "[■■■■■■■□□□]", "[■■■■■■■■□□]", "[■■■■■■■■■□]", "[■■■■■■■■■■]"]

    for i in range(len(animation)):
        sleep(0.1)
        sys.stdout.write("\r" + animation[i % len(animation)])
        sys.stdout.flush()

    print("\n")


    print("\n")
    string = "[+] 1. create Qr code based on text \n[+] 2. create Qr code based on a link\n[+] 3. create Qr code to share wifi connection\n[+] 4. create QR code with a id card template \n[+] 5. decode a Qr code or Barcode \n[+] 6. send files using Qr code \n[+] 7. create dynamic QR code \n select operation -->:"

    for letter in string:
        sleep(0.01)  # In seconds
        sys.stdout.write(letter)
        sys.stdout.flush()

    def get_super(x):
        normal = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+-=()"
        super_s = "ᴬᴮᶜᴰᴱᶠᴳᴴᴵᴶᴷᴸᴹᴺᴼᴾQᴿˢᵀᵁⱽᵂˣʸᶻᵃᵇᶜᵈᵉᶠᵍʰᶦʲᵏˡᵐⁿᵒᵖ۹ʳˢᵗᵘᵛʷˣʸᶻ⁰¹²³⁴⁵⁶⁷⁸⁹⁺⁻⁼⁽⁾"
        res = x.maketrans(''.join(normal), ''.join(super_s))
        return x.translate(res)

    # display superscipt

    option = input("1" + get_super('ST') + "  2" + get_super('ND') + "  3" + get_super('RD') + " 4" + get_super('TH') + " 5"+ get_super('TH') + " 6"+ get_super("TH") +" 7"+ get_super('TH'))
    if option == "1":
        import pyqrcode

        # write text here
        text = input("enter your desired text message ...")
        sve = input("save it as:")
        sve = sve + ".png"
        # converts text to qrcode
        qr = pyqrcode.create(text)
        from tqdm import tqdm
        from time import sleep

        for i in tqdm(range(0, 100), desc="generating..."):
            sleep(.01)
        from time import sleep

        for i in tqdm(range(50, 100), desc="opening..."):
            sleep(0.01)
        # write file name you wish to save and scale
        qr.png(sve, scale=2)
        qr.show()
        rst = input("restart? (y/n)")
        if rst == "y":
            restart()
            print("")
        elif rst == "n":

            print("Disconnecting  Console ...:")

            # animation = ["10%", "20%", "30%", "40%", "50%", "60%", "70%", "80%", "90%", "100%"]
            animation = ["[■□□□□□□□□□]", "[■■□□□□□□□□]", "[■■■□□□□□□□]", "[■■■■□□□□□□]", "[■■■■■□□□□□]", "[■■■■■■□□□□]",
                         "[■■■■■■■□□□]", "[■■■■■■■■□□]", "[■■■■■■■■■□]", "[■■■■■■■■■■]"]

            for i in range(len(animation)):
                sleep(0.02)
                sys.stdout.write("\r" + animation[i % len(animation)])
                sys.stdout.flush()

            print("\n")
            print("done...")
    elif option == "2":
        import pyqrcode

        # write text here
        url = input("enter a valid link ...")
        sve = input("save it as:")
        sve = sve + ".png"
        # converts text to qrcode
        qr = pyqrcode.create(url)
        from tqdm import tqdm
        from time import sleep

        for i in tqdm(range(0, 100), desc="generating..."):
            sleep(.01)
        from time import sleep

        for i in tqdm(range(50, 100), desc="opening..."):
            sleep(0.01)
        # write file name you wish to save and scale
        qr.png(sve, scale=2)
        qr.show()
        rs1t = input("restart? (y/n)")
        if rs1t == "y":
            restart()
            print("")
        elif rs1t == "n":
            import time
            import sys

            print("Disconnecting  Console ...:")

            # animation = ["10%", "20%", "30%", "40%", "50%", "60%", "70%", "80%", "90%", "100%"]
            animation = ["[■□□□□□□□□□]", "[■■□□□□□□□□]", "[■■■□□□□□□□]", "[■■■■□□□□□□]", "[■■■■■□□□□□]", "[■■■■■■□□□□]",
                         "[■■■■■■■□□□]", "[■■■■■■■■□□]", "[■■■■■■■■■□]", "[■■■■■■■■■■]"]

            for i in range(len(animation)):
                time.sleep(0.02)
                sys.stdout.write("\r" + animation[i % len(animation)])
                sys.stdout.flush()

            print("\n")
            print("done...")
    elif option == "3":
        import wifi_qrcode_generator as qr

        name = input("enter WiFi SSID:")
        passw = input("enter WiFi password:")
        asve = input("save this as:")
        asve = asve + ".png"
        qr.wifi_qrcode(name, False, 'WPA', passw).save(asve)
        # Use wifi_qrcode() to create a QR image
        from tqdm import tqdm
        from time import sleep

        for i in tqdm(range(0, 100), desc="generating ..."):
            sleep(.01)

        # qr.wifi_qrcode('wifi name ', False, 'WPA', 'password')
        import sys
        from time import sleep

        words = "done.."
        for char in words:
            sleep(0.5)
            sys.stdout.write(char)

        rs2t = input("restart? (y/n)")
        if rs2t == "y":
            restart()
            print("")
        elif rs2t == "n":
            import time
            import sys

            print("Disconnecting  program...")

            # animation = ["10%", "20%", "30%", "40%", "50%", "60%", "70%", "80%", "90%", "100%"]
            animation = ["[■□□□□□□□□□]", "[■■□□□□□□□□]", "[■■■□□□□□□□]", "[■■■■□□□□□□]", "[■■■■■□□□□□]", "[■■■■■■□□□□]",
                         "[■■■■■■■□□□]", "[■■■■■■■■□□]", "[■■■■■■■■■□]", "[■■■■■■■■■■]"]

            for i in range(len(animation)):
                time.sleep(0.02)
                sys.stdout.write("\r" + animation[i % len(animation)])
                sys.stdout.flush()

            print("\n")
            print("done...")

    elif option =="4":
        from PIL import Image, ImageDraw, ImageFont

        image = Image.new('RGB', (1000, 900), (255, 255, 255))
        draw = ImageDraw.Draw(image)
        font = ImageFont.truetype('arial.ttf', size=45)


        import datetime
        import qrcode

        from time import sleep
        import sys

        d_date = datetime.datetime.now()
        reg_format_date = d_date.strftime("  %d-%m-%Y\t\t\t\t\t ID CARD Generator\t\t\t\t\t  %I:%M:%S %p")
        print('------------------------------------------------------------------------------------------------')
        print(reg_format_date)
        print('------------------------------------------------------------------------------------------------')
        string = "[+] All Fields are Mandatory \n[+] Avoid any kind of Spelling Mistakes \n[+] Write Everything in uppercase letters \n:"

        for letter in string:
            sleep(0.01)  # In seconds
            sys.stdout.write(letter)
            sys.stdout.flush()

        # starting position of the message

        (x, y) = (50, 50)
        message = input('\nEnter Your Company \ Institute Name: ')
        company = message
        color = 'rgb(0, 0, 0)'
        font = ImageFont.truetype('arial.ttf', size=80)
        draw.text((x, y), message, fill=color, font=font)

        # adding an unique id number. You can manually take it from user
        (x, y) = (600, 75)
        idno = input("\nEnter your ID no.")
        message = str('ID ' + str(idno))
        color = 'rgb(0, 0, 0)'  # black color
        font = ImageFont.truetype('arial.ttf', size=60)
        draw.text((x, y), message, fill=color, font=font)

        (x, y) = (50, 250)
        message = input('Enter Your Full Name: ')
        name = message
        color = 'rgb(0, 0, 0)'  # black color
        font = ImageFont.truetype('arial.ttf', size=45)
        draw.text((x, y), message, fill=color, font=font)

        (x, y) = (50, 350)
        message = input('Enter Your Gender: ')
        gen = message
        color = 'rgb(0, 0, 0)'  # black color
        draw.text((x, y), message, fill=color, font=font)
        (x, y) = (250, 350)
        message = input('Enter Your Age: ')
        color = 'rgb(0, 0, 0)'  # black color
        draw.text((x, y), message, fill=color, font=font)
        age = message

        (x, y) = (50, 450)
        message = input('Enter Your Date Of Birth: ')
        color = 'rgb(0, 0, 0)'  # black color
        draw.text((x, y), message, fill=color, font=font)
        dob = message
        (x, y) = (50, 550)
        message = input('Enter Your Blood Group: ')
        color = 'rgb(255, 0, 0)'  # black color
        draw.text((x, y), message, fill=color, font=font)
        blc = message
        (x, y) = (50, 650)
        message = input('Enter Your Mobile Number: ')
        temp = message
        color = 'rgb(0, 0, 0)'  # black color
        draw.text((x, y), message, fill=color, font=font)

        (x, y) = (50, 750)
        message = input('Enter Your Address: ')
        color = 'rgb(0, 0, 0)'  # black color
        draw.text((x, y), message, fill=color, font=font)
        adr = message
        # save the edited image
        conc = "\n Contact no. :" + temp + "\n" + dob + "\n Blood Group :" + blc + "\n" + gen
        image.save(str(name) + '.png')

        img = qrcode.make(
            str(company) + "_" + str(idno) + str(conc))  # this info. is added in QR code, also add other things
        img.save(str(idno) + '.bmp')

        til = Image.open(name + '.png')
        im = Image.open(str(idno) + '.bmp')  # 25x25
        til.paste(im, (500, 230))
        til.save(name + '.png')

        print(('\n\n\nYour ID Card Successfully created in a PNG file ' + name + '.png'))
        sh = input("show card ? (y/n)")
        if sh == "y":
            til.show()
        elif sh == "n":
            print("ok")

        rs3t = input("restart ? (y/n)")
        if rs3t == "y":
            restart()
        elif rs3t == "n":
            import time
            import sys

            print("Disconnecting  Console ...:")

            # animation = ["10%", "20%", "30%", "40%", "50%", "60%", "70%", "80%", "90%", "100%"]
            animation = ["[■□□□□□□□□□]", "[■■□□□□□□□□]", "[■■■□□□□□□□]", "[■■■■□□□□□□]", "[■■■■■□□□□□]", "[■■■■■■□□□□]",
                         "[■■■■■■■□□□]", "[■■■■■■■■□□]", "[■■■■■■■■■□]", "[■■■■■■■■■■]"]

            for i in range(len(animation)):
                time.sleep(0.02)
                sys.stdout.write("\r" + animation[i % len(animation)])
                sys.stdout.flush()

            print("\n")
            print("done...")
    elif option =="5":
        from pyzbar import pyzbar
        import cv2
        opin30 = input("scan Qr code using Camera Vision or scan a image ?(cv/scan)")
        if opin30 == "scan":

          import pyzbar.pyzbar as pyzbar

          import cv2
          import time

          animation = ["[■□□□□□□□□□]", "[■■□□□□□□□□]", "[■■■□□□□□□□]", "[■■■■□□□□□□]", "[■■■■■□□□□□]", "[■■■■■■□□□□]",
                     "[■■■■■■■□□□]", "[■■■■■■■■□□]", "[■■■■■■■■■□]", "[■■■■■■■■■■]"]

          for i in range(len(animation)):
            time.sleep(0.04)
            sys.stdout.write("\r" + animation[i % len(animation)])
            sys.stdout.flush()



            lao = input("\nenter file name:")

            img_path = lao

            img = cv2.imread(img_path)

            barcodes = pyzbar.decode(img)

            for barcode in barcodes:
                (x, y, w, h) = barcode.rect
                cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 2)
                barcodeData = barcode.data.decode("utf-8")
                barcodeType = barcode.type
                text = "{} ({})".format(barcodeData, barcodeType)
                cv2.putText(img, text, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)
                print("[INFO] found {} barcode {}\n:".format(barcodeType, barcodeData))
            rsrt = input("restart ? (y/n)")
            if rsrt == "y":
                restart()
            elif rsrt == "n":
                import time
                import sys

                print("Disconnecting  Console ...:")

                # animation = ["10%", "20%", "30%", "40%", "50%", "60%", "70%", "80%", "90%", "100%"]
                animation = ["[■□□□□□□□□□]", "[■■□□□□□□□□]", "[■■■□□□□□□□]", "[■■■■□□□□□□]", "[■■■■■□□□□□]",
                             "[■■■■■■□□□□]",
                             "[■■■■■■■□□□]", "[■■■■■■■■□□]", "[■■■■■■■■■□]", "[■■■■■■■■■■]"]

                for i in range(len(animation)):
                    time.sleep(0.02)
                    sys.stdout.write("\r" + animation[i % len(animation)])
                    sys.stdout.flush()

                print("\n")
                print("done...")
        elif opin30 =="cv":
            import pyzbar.pyzbar as pyzbar
            import numpy as np
            import cv2
            import time
            cap = cv2.VideoCapture(0)

            cap.set(3, 640)
            cap.set(4, 480)

            # 160.0 x 120.0
            # 176.0 x 144.0
            # 320.0 x 240.0
            # 352.0 x 288.0
            # 640.0 x 480.0
            # 1024.0 x 768.0
            # 1280.0 x 1024.0
            time.sleep(2)

            def decode(im):
                decodedObjects = pyzbar.decode(im)
                # Print results
                for obj in decodedObjects:
                    print('Type : ', obj.type)
                    print('Data : ', obj.data, '\n')
                return decodedObjects
                # Find barcodes and QR codes

            font = cv2.FONT_HERSHEY_SIMPLEX

            while (cap.isOpened()):
                # Capture frame-by-frame
                ret, frame = cap.read()
                # Our operations on the frame come here
                im = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

                decodedObjects = decode(im)

                for decodedObject in decodedObjects:
                    points = decodedObject.polygon

                    # If the points do not form a quad, find convex hull
                    if len(points) > 4:
                        hull = cv2.convexHull(np.array([point for point in points], dtype=np.float32))
                        hull = list(map(tuple, np.squeeze(hull)))
                    else:
                        hull = points

                    # Number of points in the convex hull
                    n = len(hull)
                    # Draw the convext hull
                    for j in range(0, n):
                        cv2.line(frame, hull[j], hull[(j + 1) % n], (255, 0, 0), 3)

                    x = decodedObject.rect.left
                    y = decodedObject.rect.top

                    print(x, y)

                    print('Type : ', decodedObject.type)
                    print('Data : ', decodedObject.data, '\n')

                    barCode = str(decodedObject.data)
                    cv2.putText(frame, barCode, (x, y), font, 1, (0, 255, 255), 2, cv2.LINE_AA)

                # Display the resulting frame
                cv2.imshow('frame', frame)
                key = cv2.waitKey(1)
                if key & 0xFF == ord('q'):
                    break
                elif key & 0xFF == ord('s'):  # wait for 's' key to save
                    cv2.imwrite('Capture.png', frame)

            cap.release()
            cv2.destroyAllWindows()

    elif option == "6":



        import http.server

        # provides access to the BSD socket interface
        import socket

        # a framework for network servers
        import socketserver

        # to display a Web-based documents to users
        import webbrowser

        # to generate qrcode
        import pyqrcode
        from pyqrcode import QRCode

        # convert into png format
        import png

        # to access operating system control
        import os

        # assigning the appropriate port value
        PORT = 8010
        # this finds the name of the computer user
        os.environ['USERPROFILE']

        # changing the directory to access the files desktop
        # with the help of os module
        desktop = os.path.join(os.path.join(os.environ['USERPROFILE']),
                               'OneDrive')
        os.chdir(desktop)

        # creating a http request
        Handler = http.server.SimpleHTTPRequestHandler
        # returns, host name of the system under
        # which Python interpreter is executed
        hostname = socket.gethostname()

        # finding the IP address of the PC
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        IP = "http://" + s.getsockname()[0] + ":" + str(PORT)
        link = IP

        # converting the IP address into the form of a QRcode
        # with the help of pyqrcode module

        # converts the IP address into a Qrcode
        url = pyqrcode.create(link)
        # saves the Qrcode inform of svg
        url.svg("myqr.svg", scale=8)
        # opens the Qrcode image in the web browser
        webbrowser.open('myqr.svg')

        # Creating the HTTP request and serving the
        # folder in the PORT 8010,and the pyqrcode is generated

        # continuous stream of data between client and server
        with socketserver.TCPServer(("", PORT), Handler) as httpd:
            print("serving at port", PORT)
            print("Type this in your Browser", IP)
            print("or Use the QRCode")
            httpd.serve_forever()

        rs3t = input("restart ? (y/n)")
        if rs3t == "y":
            restart()
        elif rs3t == "n":
            import time
            import sys

            print("Disconnecting  Console ...:")

            # animation = ["10%", "20%", "30%", "40%", "50%", "60%", "70%", "80%", "90%", "100%"]
            animation = ["[■□□□□□□□□□]", "[■■□□□□□□□□]", "[■■■□□□□□□□]", "[■■■■□□□□□□]", "[■■■■■□□□□□]", "[■■■■■■□□□□]",
                         "[■■■■■■■□□□]", "[■■■■■■■■□□]", "[■■■■■■■■■□]", "[■■■■■■■■■■]"]

            for i in range(len(animation)):
                time.sleep(0.02)
                sys.stdout.write("\r" + animation[i % len(animation)])
                sys.stdout.flush()

            print("\n")
            print("done...")
        elif option == "7":
            from MyQR import myqr
            import os
            import time
            print("starting dynamic Console ...:")

            # animation = ["10%", "20%", "30%", "40%", "50%", "60%", "70%", "80%", "90%", "100%"]
            animation = ["[■□□□□□□□□□]", "[■■□□□□□□□□]", "[■■■□□□□□□□]", "[■■■■□□□□□□]", "[■■■■■□□□□□]", "[■■■■■■□□□□]",
                         "[■■■■■■■□□□]", "[■■■■■■■■□□]", "[■■■■■■■■■□]", "[■■■■■■■■■■]"]

            for i in range(len(animation)):
                time.sleep(0.02)
                sys.stdout.write("\r" + animation[i % len(animation)])
                sys.stdout.flush()

            string = "\na gif file is needed to create dynamic QR code\n"

            for letter in string:
                sleep(0.01)  # In seconds
                sys.stdout.write(letter)
                sys.stdout.flush()

            cl = input("colorised?(y/n)")
            if cl == "y":

                version, level, qr_name = myqr.run(

                    words=input("\nenter text message or url"),
                    version=6,

                    level='H',

                    picture=input("enter gif file name") + ".gif",

                    # Color QR code
                    colorized=True,
                    contrast=1.0,
                    brightness=1.0,
                    save_name=input("save it as:") + ".gif",
                    save_dir=os.getcwd()

                )
                animation = ["[■□□□□□□□□□]", "[■■□□□□□□□□]", "[■■■□□□□□□□]", "[■■■■□□□□□□]", "[■■■■■□□□□□]",
                             "[■■■■■■□□□□]",
                             "[■■■■■■■□□□]", "[■■■■■■■■□□]", "[■■■■■■■■■□]", "[■■■■■■■■■■]"]

                for i in range(len(animation)):
                    time.sleep(0.02)
                    sys.stdout.write("\r" + animation[i % len(animation)])
                    sys.stdout.flush()
                rs3t = input("\nrestart ? (y/n)")
                if rs3t == "y":
                    restart()
                elif rs3t == "n":
                    import time
                    import sys

                    print("Disconnecting  Console ...:")

                    # animation = ["10%", "20%", "30%", "40%", "50%", "60%", "70%", "80%", "90%", "100%"]
                    animation = ["[■□□□□□□□□□]", "[■■□□□□□□□□]", "[■■■□□□□□□□]", "[■■■■□□□□□□]", "[■■■■■□□□□□]",
                                 "[■■■■■■□□□□]",
                                 "[■■■■■■■□□□]", "[■■■■■■■■□□]", "[■■■■■■■■■□]", "[■■■■■■■■■■]"]

                    for i in range(len(animation)):
                        time.sleep(0.02)
                        sys.stdout.write("\r" + animation[i % len(animation)])
                        sys.stdout.flush()

                    print("\n")
                    print("done...")
            if cl == "n":
                version, level, qr_name = myqr.run(

                    words=input("\nenter text message or url"),
                    version=6,

                    level='H',

                    picture=input("enter gif file name") + ".gif",

                    # Color QR code
                    colorized=False,
                    contrast=1.0,
                    brightness=1.0,
                    save_name=input("save it as:") + ".gif",
                    save_dir=os.getcwd()

                )
                animation = ["[■□□□□□□□□□]", "[■■□□□□□□□□]", "[■■■□□□□□□□]", "[■■■■□□□□□□]", "[■■■■■□□□□□]",
                             "[■■■■■■□□□□]",
                             "[■■■■■■■□□□]", "[■■■■■■■■□□]", "[■■■■■■■■■□]", "[■■■■■■■■■■]"]

                for i in range(len(animation)):
                    time.sleep(0.02)
                    sys.stdout.write("\r" + animation[i % len(animation)])
                    sys.stdout.flush()
                rs3t = input("\nrestart ? (y/n)")
                if rs3t == "y":
                    restart()
                elif rs3t == "n":
                    import time
                    import sys

                    print("Disconnecting  Console ...:")

                    # animation = ["10%", "20%", "30%", "40%", "50%", "60%", "70%", "80%", "90%", "100%"]
                    animation = ["[■□□□□□□□□□]", "[■■□□□□□□□□]", "[■■■□□□□□□□]", "[■■■■□□□□□□]", "[■■■■■□□□□□]",
                                 "[■■■■■■□□□□]",
                                 "[■■■■■■■□□□]", "[■■■■■■■■□□]", "[■■■■■■■■■□]", "[■■■■■■■■■■]"]

                    for i in range(len(animation)):
                        time.sleep(0.02)
                        sys.stdout.write("\r" + animation[i % len(animation)])
                        sys.stdout.flush()

                    print("\n")
                    print("done...")

    elif option == "ss":
        spec()

    elif option == "cr":
        cr()

    else:
        restart1()























def restart1():
    from time import sleep
    import sys

    for i in range(21):
        sys.stdout.write('\r')
        # the exact output you're looking for:
        sys.stdout.write("[%-20s] %d%%" % ('ᴵ' * i, 5 * i))
        sys.stdout.flush()
        sleep(0.05)

    string = "\nR1SH4BH\n"

    for letter in string:
        sleep(0.01)  # In seconds
        sys.stdout.write(letter)
        sys.stdout.flush()

    import sys

    print("restarting program in...")
    string = " \n3...\n2...\n1....\nreconnecting...\n"

    for letter in string:
        sleep(0.1)  # In seconds
        sys.stdout.write(letter)
        sys.stdout.flush()
    import time
    import sys

    animation = "|/-\\"

    for i in range(100):
        time.sleep(0.01)
        sys.stdout.write("\r" + animation[i % len(animation)])
        sys.stdout.flush()
    # animation = ["10%", "20%", "30%", "40%", "50%", "60%", "70%", "80%", "90%", "100%"]
    animation = ["[■□□□□□□□□□]", "[■■□□□□□□□□]", "[■■■□□□□□□□]", "[■■■■□□□□□□]", "[■■■■■□□□□□]", "[■■■■■■□□□□]",
                 "[■■■■■■■□□□]", "[■■■■■■■■□□]", "[■■■■■■■■■□]", "[■■■■■■■■■■]"]

    for i in range(len(animation)):
        time.sleep(0.1)
        sys.stdout.write("\r" + animation[i % len(animation)])
        sys.stdout.flush()

    string = "\nrecalling directory...\n"

    for letter in string:
        sleep(0.01)  # In seconds
        sys.stdout.write(letter)
        sys.stdout.flush()


    # animation = ["10%", "20%", "30%", "40%", "50%", "60%", "70%", "80%", "90%", "100%"]
    animation = ["[■□□□□□□□□□]", "[■■□□□□□□□□]", "[■■■□□□□□□□]", "[■■■■□□□□□□]", "[■■■■■□□□□□]", "[■■■■■■□□□□]",
                 "[■■■■■■■□□□]", "[■■■■■■■■□□]", "[■■■■■■■■■□]", "[■■■■■■■■■■]"]

    for i in range(len(animation)):
        time.sleep(0.01)
        sys.stdout.write("\r" + animation[i % len(animation)])
        sys.stdout.flush()

    print("\n")
    string = "\n--------------------------------------------\n"

    for letter in string:
        sleep(0.01)  # In seconds
        sys.stdout.write(letter)
        sys.stdout.flush()

    string ="[+] 1. create Qr code based on text \n[+] 2. create Qr code based on a link\n[+] 3. create Qr code to share wifi connection\n[+] 4. create QR code with a id card template \n[+] 5. decode a Qr code or Barcode \n[+] 6. send files using Qr code \n[+] 7. create dynamic QR code\n select operation -->:"




    for letter in string:
        sleep(0.01)  # In seconds
        sys.stdout.write(letter)
        sys.stdout.flush()

    def get_super(x):
        normal = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+-=()"
        super_s = "ᴬᴮᶜᴰᴱᶠᴳᴴᴵᴶᴷᴸᴹᴺᴼᴾQᴿˢᵀᵁⱽᵂˣʸᶻᵃᵇᶜᵈᵉᶠᵍʰᶦʲᵏˡᵐⁿᵒᵖ۹ʳˢᵗᵘᵛʷˣʸᶻ⁰¹²³⁴⁵⁶⁷⁸⁹⁺⁻⁼⁽⁾"
        res = x.maketrans(''.join(normal), ''.join(super_s))
        return x.translate(res)

    # display superscipt

    option = input("1" + get_super('ST') + "  2" + get_super('ND') + "  3" + get_super('RD') + " 4" + get_super('TH') + " 5"+ get_super('TH')+ " 6"+ get_super("TH") +" 7"+ get_super('TH'))
    if option == "1":
        import pyqrcode

        # write text here
        text = input("enter your desired text message ...")
        sve = input("save it as:")
        sve = sve + ".png"
        # converts text to qrcode
        qr = pyqrcode.create(text)
        from tqdm import tqdm
        from time import sleep

        for i in tqdm(range(0, 100), desc="generating..."):
            sleep(.01)
        from time import sleep

        for i in tqdm(range(50, 100), desc="opening..."):
            sleep(0.01)
        # write file name you wish to save and scale
        qr.png(sve, scale=2)
        qr.show()
        rst = input("restart? (y/n)")
        if rst == "y":
            restart()
            print("")
        elif rst == "n":

            print("Disconnecting  Console ...:")

            # animation = ["10%", "20%", "30%", "40%", "50%", "60%", "70%", "80%", "90%", "100%"]
            animation = ["[■□□□□□□□□□]", "[■■□□□□□□□□]", "[■■■□□□□□□□]", "[■■■■□□□□□□]", "[■■■■■□□□□□]", "[■■■■■■□□□□]",
                         "[■■■■■■■□□□]", "[■■■■■■■■□□]", "[■■■■■■■■■□]", "[■■■■■■■■■■]"]

            for i in range(len(animation)):
                time.sleep(0.02)
                sys.stdout.write("\r" + animation[i % len(animation)])
                sys.stdout.flush()

            print("\n")
            print("done...")
    elif option == "2":
        import pyqrcode

        # write text here
        url = input("enter a valid link ...")
        sve = input("save it as:")
        sve = sve + ".png"
        # converts text to qrcode
        qr = pyqrcode.create(url)
        from tqdm import tqdm
        from time import sleep

        for i in tqdm(range(0, 100), desc="generating..."):
            sleep(.01)
        from time import sleep

        for i in tqdm(range(50, 100), desc="opening..."):
            sleep(0.01)
        # write file name you wish to save and scale
        qr.png(sve, scale=2)
        qr.show()
        rs1t = input("restart? (y/n)")
        if rs1t == "y":
            restart()
            print("")
        elif rs1t == "n":
            import time
            import sys

            print("Disconnecting  Console ...:")

            # animation = ["10%", "20%", "30%", "40%", "50%", "60%", "70%", "80%", "90%", "100%"]
            animation = ["[■□□□□□□□□□]", "[■■□□□□□□□□]", "[■■■□□□□□□□]", "[■■■■□□□□□□]", "[■■■■■□□□□□]", "[■■■■■■□□□□]",
                         "[■■■■■■■□□□]", "[■■■■■■■■□□]", "[■■■■■■■■■□]", "[■■■■■■■■■■]"]

            for i in range(len(animation)):
                time.sleep(0.02)
                sys.stdout.write("\r" + animation[i % len(animation)])
                sys.stdout.flush()

            print("\n")
            print("done...")
    elif option == "3":
        import wifi_qrcode_generator as qr

        name = input("enter WiFi SSID:")
        passw = input("enter WiFi password:")
        asve = input("save this as:")
        asve = asve + ".png"
        qr.wifi_qrcode(name, False, 'WPA', passw).save(asve)
        # Use wifi_qrcode() to create a QR image
        from tqdm import tqdm
        from time import sleep

        for i in tqdm(range(0, 100), desc="generating ..."):
            sleep(.01)

        # qr.wifi_qrcode('wifi name ', False, 'WPA', 'password')
        import sys
        from time import sleep

        words = "done.."
        for char in words:
            sleep(0.5)
            sys.stdout.write(char)

        rs2t = input("restart? (y/n)")
        if rs2t == "y":
            restart()
            print("")
        elif rs2t == "n":
            import time
            import sys

            print("Disconnecting  program...")

            # animation = ["10%", "20%", "30%", "40%", "50%", "60%", "70%", "80%", "90%", "100%"]
            animation = ["[■□□□□□□□□□]", "[■■□□□□□□□□]", "[■■■□□□□□□□]", "[■■■■□□□□□□]", "[■■■■■□□□□□]", "[■■■■■■□□□□]",
                         "[■■■■■■■□□□]", "[■■■■■■■■□□]", "[■■■■■■■■■□]", "[■■■■■■■■■■]"]

            for i in range(len(animation)):
                time.sleep(0.01 )
                sys.stdout.write("\r" + animation[i % len(animation)])
                sys.stdout.flush()

            print("\n")
            print("done...")

    elif option == "4":
        from PIL import Image, ImageDraw, ImageFont

        image = Image.new('RGB', (1000, 900), (255, 255, 255))
        draw = ImageDraw.Draw(image)
        font = ImageFont.truetype('arial.ttf', size=45)


        import datetime
        import qrcode

        from time import sleep
        import sys

        d_date = datetime.datetime.now()
        reg_format_date = d_date.strftime("  %d-%m-%Y\t\t\t\t\t ID CARD Generator\t\t\t\t\t  %I:%M:%S %p")
        print('------------------------------------------------------------------------------------------------')
        print(reg_format_date)
        print('------------------------------------------------------------------------------------------------')
        string = "[+] All Fields are Mandatory \n[+] Avoid any kind of Spelling Mistakes \n[+] Write Everything in uppercase letters \n:"

        for letter in string:
            sleep(0.01)  # In seconds
            sys.stdout.write(letter)
            sys.stdout.flush()

        # starting position of the message

        (x, y) = (50, 50)
        message = input('\nEnter Your Company \ Institute Name: ')
        company = message
        color = 'rgb(0, 0, 0)'
        font = ImageFont.truetype('arial.ttf', size=80)
        draw.text((x, y), message, fill=color, font=font)

        # adding an unique id number. You can manually take it from user
        (x, y) = (600, 75)
        idno = input("\nEnter your ID no.")
        message = str('ID ' + str(idno))
        color = 'rgb(0, 0, 0)'  # black color
        font = ImageFont.truetype('arial.ttf', size=60)
        draw.text((x, y), message, fill=color, font=font)

        (x, y) = (50, 250)
        message = input('Enter Your Full Name: ')
        name = message
        color = 'rgb(0, 0, 0)'  # black color
        font = ImageFont.truetype('arial.ttf', size=45)
        draw.text((x, y), message, fill=color, font=font)

        (x, y) = (50, 350)
        message = input('Enter Your Gender: ')
        gen = message
        color = 'rgb(0, 0, 0)'  # black color
        draw.text((x, y), message, fill=color, font=font)
        (x, y) = (250, 350)
        message = input('Enter Your Age: ')
        color = 'rgb(0, 0, 0)'  # black color
        draw.text((x, y), message, fill=color, font=font)
        age = message

        (x, y) = (50, 450)
        message = input('Enter Your Date Of Birth: ')
        color = 'rgb(0, 0, 0)'  # black color
        draw.text((x, y), message, fill=color, font=font)
        dob = message
        (x, y) = (50, 550)
        message = input('Enter Your Blood Group: ')
        color = 'rgb(255, 0, 0)'  # black color
        draw.text((x, y), message, fill=color, font=font)
        blc = message
        (x, y) = (50, 650)
        message = input('Enter Your Mobile Number: ')
        temp = message
        color = 'rgb(0, 0, 0)'  # black color
        draw.text((x, y), message, fill=color, font=font)

        (x, y) = (50, 750)
        message = input('Enter Your Address: ')
        color = 'rgb(0, 0, 0)'  # black color
        draw.text((x, y), message, fill=color, font=font)
        adr = message
        # save the edited image
        conc = "\n Contact no. :" + temp + "\n" + dob + "\n Blood Group :" + blc + "\n" + gen
        image.save(str(name) + '.png')

        img = qrcode.make(
            str(company) + "_" + str(idno) + str(conc))  # this info. is added in QR code, also add other things
        img.save(str(idno) + '.bmp')

        til = Image.open(name + '.png')
        im = Image.open(str(idno) + '.bmp')  # 25x25
        til.paste(im, (500, 230))
        til.save(name + '.png')

        print(('\n\n\nYour ID Card Successfully created in a PNG file ' + name + '.png'))
        sh = input("show card ? (y/n)")
        if sh == "y":
            til.show()
        elif sh == "n":
            print("ok")

        rs3t = input("restart ? (y/n)")
        if rs3t == "y":
            restart()
        elif rs3t == "n":
            import time
            import sys

            print("Disconnecting  Console ...:")

            # animation = ["10%", "20%", "30%", "40%", "50%", "60%", "70%", "80%", "90%", "100%"]
            animation = ["[■□□□□□□□□□]", "[■■□□□□□□□□]", "[■■■□□□□□□□]", "[■■■■□□□□□□]", "[■■■■■□□□□□]", "[■■■■■■□□□□]",
                         "[■■■■■■■□□□]", "[■■■■■■■■□□]", "[■■■■■■■■■□]", "[■■■■■■■■■■]"]

            for i in range(len(animation)):
                time.sleep(0.02)
                sys.stdout.write("\r" + animation[i % len(animation)])
                sys.stdout.flush()

            print("\n")
            print("done...")
        # End

        # End
    elif option =="5":
        from pyzbar import pyzbar
        import cv2
        opin30 = input("scan Qr code using Camera Vision or scan a image ?(cv/scan)")
        if opin30 == "scan":

            import pyzbar.pyzbar as pyzbar

            import cv2
            import time

            animation = ["[■□□□□□□□□□]", "[■■□□□□□□□□]", "[■■■□□□□□□□]", "[■■■■□□□□□□]", "[■■■■■□□□□□]", "[■■■■■■□□□□]",
                         "[■■■■■■■□□□]", "[■■■■■■■■□□]", "[■■■■■■■■■□]", "[■■■■■■■■■■]"]

            for i in range(len(animation)):
                time.sleep(0.04)
                sys.stdout.write("\r" + animation[i % len(animation)])
                sys.stdout.flush()

                lao = input("\nenter file name:")

                img_path = lao

                img = cv2.imread(img_path)

                barcodes = pyzbar.decode(img)

                for barcode in barcodes:
                    (x, y, w, h) = barcode.rect
                    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 2)
                    barcodeData = barcode.data.decode("utf-8")
                    barcodeType = barcode.type
                    text = "{} ({})".format(barcodeData, barcodeType)
                    cv2.putText(img, text, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)
                    print("[INFO] found {} barcode {}\n:".format(barcodeType, barcodeData))
                rsrt = input("restart ? (y/n)")
                if rsrt == "y":
                    restart()
                elif rsrt == "n":
                    import time
                    import sys

                    print("Disconnecting  Console ...:")

                    # animation = ["10%", "20%", "30%", "40%", "50%", "60%", "70%", "80%", "90%", "100%"]
                    animation = ["[■□□□□□□□□□]", "[■■□□□□□□□□]", "[■■■□□□□□□□]", "[■■■■□□□□□□]", "[■■■■■□□□□□]",
                                 "[■■■■■■□□□□]",
                                 "[■■■■■■■□□□]", "[■■■■■■■■□□]", "[■■■■■■■■■□]", "[■■■■■■■■■■]"]

                    for i in range(len(animation)):
                        time.sleep(0.02)
                        sys.stdout.write("\r" + animation[i % len(animation)])
                        sys.stdout.flush()

                    print("\n")
                    print("done...")
        elif opin30 == "cv":
            import pyzbar.pyzbar as pyzbar
            import numpy as np
            import cv2
            import time
            cap = cv2.VideoCapture(0)

            cap.set(3, 640)
            cap.set(4, 480)

            # 160.0 x 120.0
            # 176.0 x 144.0
            # 320.0 x 240.0
            # 352.0 x 288.0
            # 640.0 x 480.0
            # 1024.0 x 768.0
            # 1280.0 x 1024.0
            time.sleep(2)

            def decode(im):
                decodedObjects = pyzbar.decode(im)
                # Print results
                for obj in decodedObjects:
                    print('Type : ', obj.type)
                    print('Data : ', obj.data, '\n')
                return decodedObjects
                # Find barcodes and QR codes

            font = cv2.FONT_HERSHEY_SIMPLEX

            while (cap.isOpened()):
                # Capture frame-by-frame
                ret, frame = cap.read()
                # Our operations on the frame come here
                im = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

                decodedObjects = decode(im)

                for decodedObject in decodedObjects:
                    points = decodedObject.polygon

                    # If the points do not form a quad, find convex hull
                    if len(points) > 4:
                        hull = cv2.convexHull(np.array([point for point in points], dtype=np.float32))
                        hull = list(map(tuple, np.squeeze(hull)))
                    else:
                        hull = points

                    # Number of points in the convex hull
                    n = len(hull)
                    # Draw the convext hull
                    for j in range(0, n):
                        cv2.line(frame, hull[j], hull[(j + 1) % n], (255, 0, 0), 3)

                    x = decodedObject.rect.left
                    y = decodedObject.rect.top

                    print(x, y)

                    print('Type : ', decodedObject.type)
                    print('Data : ', decodedObject.data, '\n')

                    barCode = str(decodedObject.data)
                    cv2.putText(frame, barCode, (x, y), font, 1, (0, 255, 255), 2, cv2.LINE_AA)

                # Display the resulting frame
                cv2.imshow('frame', frame)
                key = cv2.waitKey(1)
                if key & 0xFF == ord('q'):
                    break
                elif key & 0xFF == ord('s'):  # wait for 's' key to save
                    cv2.imwrite('Capture.png', frame)

            cap.release()
            cv2.destroyAllWindows()




    elif option == "6":
        # import necessary modules

        # for implementing the HTTP Web servers
        import http.server

        # provides access to the BSD socket interface
        import socket

        # a framework for network servers
        import socketserver

        # to display a Web-based documents to users
        import webbrowser

        # to generate qrcode
        import pyqrcode
        from pyqrcode import QRCode

        # convert into png format
        import png

        # to access operating system control
        import os

        # assigning the appropriate port value
        PORT = 8010
        # this finds the name of the computer user
        os.environ['USERPROFILE']

        # changing the directory to access the files desktop
        # with the help of os module
        desktop = os.path.join(os.path.join(os.environ['USERPROFILE']),
                               'OneDrive')
        os.chdir(desktop)

        # creating a http request
        Handler = http.server.SimpleHTTPRequestHandler
        # returns, host name of the system under
        # which Python interpreter is executed
        hostname = socket.gethostname()

        # finding the IP address of the PC
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        IP = "http://" + s.getsockname()[0] + ":" + str(PORT)
        link = IP

        # converting the IP address into the form of a QRcode
        # with the help of pyqrcode module

        # converts the IP address into a Qrcode
        url = pyqrcode.create(link)
        # saves the Qrcode inform of svg
        url.svg("myqr.svg", scale=8)
        # opens the Qrcode image in the web browser
        webbrowser.open('myqr.svg')

        # Creating the HTTP request and serving the
        # folder in the PORT 8010,and the pyqrcode is generated

        # continuous stream of data between client and server
        with socketserver.TCPServer(("", PORT), Handler) as httpd:
            print("serving at port", PORT)
            print("Type this in your Browser", IP)
            print("or Use the QRCode")
            httpd.serve_forever()

        rs3t = input("restart ? (y/n)")
        if rs3t == "y":
            restart()
        elif rs3t == "n":
            import time
            import sys

            print("Disconnecting  Console ...:")

            # animation = ["10%", "20%", "30%", "40%", "50%", "60%", "70%", "80%", "90%", "100%"]
            animation = ["[■□□□□□□□□□]", "[■■□□□□□□□□]", "[■■■□□□□□□□]", "[■■■■□□□□□□]", "[■■■■■□□□□□]", "[■■■■■■□□□□]",
                         "[■■■■■■■□□□]", "[■■■■■■■■□□]", "[■■■■■■■■■□]", "[■■■■■■■■■■]"]

            for i in range(len(animation)):
                time.sleep(0.02)
                sys.stdout.write("\r" + animation[i % len(animation)])
                sys.stdout.flush()

            print("\n")
            print("done...")


    elif option == "7":

        from MyQR import myqr

        import os

        print("starting dynamic Console ...:")

        # animation = ["10%", "20%", "30%", "40%", "50%", "60%", "70%", "80%", "90%", "100%"]

        animation = ["[■□□□□□□□□□]", "[■■□□□□□□□□]", "[■■■□□□□□□□]", "[■■■■□□□□□□]", "[■■■■■□□□□□]", "[■■■■■■□□□□]",

                     "[■■■■■■■□□□]", "[■■■■■■■■□□]", "[■■■■■■■■■□]", "[■■■■■■■■■■]"]

        for i in range(len(animation)):
            time.sleep(0.02)

            sys.stdout.write("\r" + animation[i % len(animation)])

            sys.stdout.flush()

        string = "\na gif file is needed to create dynamic QR code\n"

        for letter in string:
            sleep(0.01)  # In seconds

            sys.stdout.write(letter)

            sys.stdout.flush()

        cl = input("colorised?(y/n)")

        if cl == "y":

            version, level, qr_name = myqr.run(

                words=input("\nenter text message or url"),

                version=6,

                level='H',

                picture=input("enter gif file name") + ".gif",

                # Color QR code

                colorized=True,

                contrast=1.0,

                brightness=1.0,

                save_name=input("save it as:") + ".gif",

                save_dir=os.getcwd()

            )

            animation = ["[■□□□□□□□□□]", "[■■□□□□□□□□]", "[■■■□□□□□□□]", "[■■■■□□□□□□]", "[■■■■■□□□□□]", "[■■■■■■□□□□]",

                         "[■■■■■■■□□□]", "[■■■■■■■■□□]", "[■■■■■■■■■□]", "[■■■■■■■■■■]"]

            for i in range(len(animation)):
                time.sleep(0.02)

                sys.stdout.write("\r" + animation[i % len(animation)])

                sys.stdout.flush()

            rs3t = input("\nrestart ? (y/n)")

            if rs3t == "y":

                restart()

            elif rs3t == "n":

                import time

                import sys

                print("Disconnecting  Console ...:")

                # animation = ["10%", "20%", "30%", "40%", "50%", "60%", "70%", "80%", "90%", "100%"]

                animation = ["[■□□□□□□□□□]", "[■■□□□□□□□□]", "[■■■□□□□□□□]", "[■■■■□□□□□□]", "[■■■■■□□□□□]",
                             "[■■■■■■□□□□]",

                             "[■■■■■■■□□□]", "[■■■■■■■■□□]", "[■■■■■■■■■□]", "[■■■■■■■■■■]"]

                for i in range(len(animation)):
                    time.sleep(0.02)

                    sys.stdout.write("\r" + animation[i % len(animation)])

                    sys.stdout.flush()

                print("\n")

                print("done...")

        if cl == "n":

            version, level, qr_name = myqr.run(

                words=input("\nenter text message or url"),

                version=6,

                level='H',

                picture=input("enter gif file name") + ".gif",

                # Color QR code

                colorized=False,

                contrast=1.0,

                brightness=1.0,

                save_name=input("save it as:") + ".gif",

                save_dir=os.getcwd()

            )

            animation = ["[■□□□□□□□□□]", "[■■□□□□□□□□]", "[■■■□□□□□□□]", "[■■■■□□□□□□]", "[■■■■■□□□□□]", "[■■■■■■□□□□]",

                         "[■■■■■■■□□□]", "[■■■■■■■■□□]", "[■■■■■■■■■□]", "[■■■■■■■■■■]"]

            for i in range(len(animation)):
                time.sleep(0.02)

                sys.stdout.write("\r" + animation[i % len(animation)])

                sys.stdout.flush()

            rs3t = input("\nrestart ? (y/n)")

            if rs3t == "y":

                restart()

            elif rs3t == "n":

                import time

                import sys

                print("Disconnecting  Console ...:")

                # animation = ["10%", "20%", "30%", "40%", "50%", "60%", "70%", "80%", "90%", "100%"]

                animation = ["[■□□□□□□□□□]", "[■■□□□□□□□□]", "[■■■□□□□□□□]", "[■■■■□□□□□□]", "[■■■■■□□□□□]",
                             "[■■■■■■□□□□]",

                             "[■■■■■■■□□□]", "[■■■■■■■■□□]", "[■■■■■■■■■□]", "[■■■■■■■■■■]"]

                for i in range(len(animation)):
                    time.sleep(0.02)

                    sys.stdout.write("\r" + animation[i % len(animation)])

                    sys.stdout.flush()

                print("\n")

                print("done...")

    elif option == "ss":
        spec()

    elif option == "cr":
        cr()

    else:
        print("please type correct option!")
        restart1()































encodings = "UTF-8"
import sys
from time import sleep



string = "R1SH4BH\n"

for letter in string:
  sleep(0.01) # In seconds
  sys.stdout.write(letter)
  sys.stdout.flush()

import time
import sys

print("starting program...")

        # animation = ["10%", "20%", "30%", "40%", "50%", "60%", "70%", "80%", "90%", "100%"]
animation = ["[■□□□□□□□□□]", "[■■□□□□□□□□]", "[■■■□□□□□□□]", "[■■■■□□□□□□]", "[■■■■■□□□□□]", "[■■■■■■□□□□]",
                     "[■■■■■■■□□□]", "[■■■■■■■■□□]", "[■■■■■■■■■□]", "[■■■■■■■■■■]"]

for i in range(len(animation)):
    time.sleep(0.2)
    sys.stdout.write("\r" + animation[i % len(animation)])
    sys.stdout.flush()


print("\n")
print("collecting modules ...")

        # animation = ["10%", "20%", "30%", "40%", "50%", "60%", "70%", "80%", "90%", "100%"]
animation = ["[■□□□□□□□□□]", "[■■□□□□□□□□]", "[■■■□□□□□□□]", "[■■■■□□□□□□]", "[■■■■■□□□□□]", "[■■■■■■□□□□]",
                     "[■■■■■■■□□□]", "[■■■■■■■■□□]", "[■■■■■■■■■□]", "[■■■■■■■■■■]"]

for i in range(len(animation)):
    time.sleep(0.1)
    sys.stdout.write("\r" + animation[i % len(animation)])
    sys.stdout.flush()


print("\n")
print("connecting to directory ...")

        # animation = ["10%", "20%", "30%", "40%", "50%", "60%", "70%", "80%", "90%", "100%"]
animation = ["[■□□□□□□□□□]", "[■■□□□□□□□□]", "[■■■□□□□□□□]", "[■■■■□□□□□□]", "[■■■■■□□□□□]", "[■■■■■■□□□□]",
                     "[■■■■■■■□□□]", "[■■■■■■■■□□]", "[■■■■■■■■■□]", "[■■■■■■■■■■]"]

for i in range(len(animation)):
    time.sleep(0.1)
    sys.stdout.write("\r" + animation[i % len(animation)])
    sys.stdout.flush()


print("\n")
string = "[+] 1. create Qr code based on text \n[+] 2. create Qr code based on a link\n[+] 3. create Qr code to share wifi connection\n[+] 4. create QR code with a id card template \n[+] 5. decode a Qr code or Barcode \n[+] 6. send files using Qr code \n[+] 7. create dynamic QR code\n select operation -->:"





for letter in string:
  sleep(0.01) # In seconds
  sys.stdout.write(letter)
  sys.stdout.flush()

def get_super(x):
            normal = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+-=()"
            super_s = "ᴬᴮᶜᴰᴱᶠᴳᴴᴵᴶᴷᴸᴹᴺᴼᴾQᴿˢᵀᵁⱽᵂˣʸᶻᵃᵇᶜᵈᵉᶠᵍʰᶦʲᵏˡᵐⁿᵒᵖ۹ʳˢᵗᵘᵛʷˣʸᶻ⁰¹²³⁴⁵⁶⁷⁸⁹⁺⁻⁼⁽⁾"
            res = x.maketrans(''.join(normal), ''.join(super_s))
            return x.translate(res)

    # display superscipt

option = input("1" + get_super('ST') + "  2" + get_super('ND') + "  3" + get_super('RD') + " 4" + get_super('TH') + " 5"+ get_super('TH')+ " 6"+ get_super("TH") +" 7"+ get_super('TH'))
if option =="1":
    import pyqrcode

    # write text here
    text = input("enter your desired text message ...")
    sve = input("save it as:")
    sve = sve+".png"
    # converts text to qrcode
    qr = pyqrcode.create(text)
    from tqdm import tqdm
    from time import sleep

    for i in tqdm(range(0, 100), desc="generating..."):
        sleep(.01)
    from time import sleep

    for i in tqdm(range(50, 100), desc="opening..."):
        sleep(0.01)
    # write file name you wish to save and scale
    qr.png(sve, scale=2)
    qr.show()
    rst = input("restart? (y/n)")
    if rst =="y":
     restart()
    elif rst =="n":
        import time
        import sys

        print("Disconnecting  Console ...:")

        # animation = ["10%", "20%", "30%", "40%", "50%", "60%", "70%", "80%", "90%", "100%"]
        animation = ["[■□□□□□□□□□]", "[■■□□□□□□□□]", "[■■■□□□□□□□]", "[■■■■□□□□□□]", "[■■■■■□□□□□]", "[■■■■■■□□□□]",
                     "[■■■■■■■□□□]", "[■■■■■■■■□□]", "[■■■■■■■■■□]", "[■■■■■■■■■■]"]

        for i in range(len(animation)):
            time.sleep(0.02)
            sys.stdout.write("\r" + animation[i % len(animation)])
            sys.stdout.flush()

        print("\n")
        print("done...")
elif option =="2":
    import pyqrcode

    # write text here
    url = input("enter a valid link ...")
    sve = input("save it as:")
    sve = sve + ".png"
    # converts text to qrcode
    qr = pyqrcode.create(url)
    from tqdm import tqdm
    from time import sleep

    for i in tqdm(range(0, 100), desc="generating..."):
        sleep(.01)
    from time import sleep

    for i in tqdm(range(50, 100), desc="opening..."):
        sleep(0.01)
    # write file name you wish to save and scale
    qr.png(sve, scale=2)
    qr.show()
    rs1t = input("restart? (y/n)")
    if rs1t == "y":

     restart()

    elif rs1t =="n":
        import time
        import sys

        print("Disconnecting  Console ...:")

        # animation = ["10%", "20%", "30%", "40%", "50%", "60%", "70%", "80%", "90%", "100%"]
        animation = ["[■□□□□□□□□□]", "[■■□□□□□□□□]", "[■■■□□□□□□□]", "[■■■■□□□□□□]", "[■■■■■□□□□□]", "[■■■■■■□□□□]",
                     "[■■■■■■■□□□]", "[■■■■■■■■□□]", "[■■■■■■■■■□]", "[■■■■■■■■■■]"]

        for i in range(len(animation)):
            time.sleep(0.02)
            sys.stdout.write("\r" + animation[i % len(animation)])
            sys.stdout.flush()

        print("\n")
        print("done...")
elif option =="3":
    import wifi_qrcode_generator as qr

    name = input("enter WiFi SSID:")
    passw = input("enter WiFi password :")
    asve = input("save this as:")
    asve = asve + ".png"
    qr.wifi_qrcode(name, False, 'WPA', passw).save(asve)
    # Use wifi_qrcode() to create a QR image
    from tqdm import tqdm
    from time import sleep

    for i in tqdm(range(0, 100), desc="generating ..."):
        sleep(.01)

    # qr.wifi_qrcode('wifi name ', False, 'WPA', 'password')
    import sys
    from time import sleep

    words = "done.."
    for char in words:
        sleep(0.5)
        sys.stdout.write(char)

    rs2t = input("restart? (y/n)")
    if rs2t == "y":

      restart()
    elif rs2t =="n":
        import time
        import sys

        print("Disconnecting  program...")

        # animation = ["10%", "20%", "30%", "40%", "50%", "60%", "70%", "80%", "90%", "100%"]
        animation = ["[■□□□□□□□□□]", "[■■□□□□□□□□]", "[■■■□□□□□□□]", "[■■■■□□□□□□]", "[■■■■■□□□□□]", "[■■■■■■□□□□]",
                     "[■■■■■■■□□□]", "[■■■■■■■■□□]", "[■■■■■■■■■□]", "[■■■■■■■■■■]"]

        for i in range(len(animation)):
            time.sleep(0.02)
            sys.stdout.write("\r" + animation[i % len(animation)])
            sys.stdout.flush()

        print("\n")
        print("done...")
elif option == "4":
        from PIL import Image, ImageDraw, ImageFont

        image = Image.new('RGB', (1000, 900), (255, 255, 255))
        draw = ImageDraw.Draw(image)
        font = ImageFont.truetype('arial.ttf', size=45)


        import datetime
        import qrcode

        from time import sleep
        import sys

        d_date = datetime.datetime.now()
        reg_format_date = d_date.strftime("  %d-%m-%Y\t\t\t\t\t ID CARD Generator\t\t\t\t\t  %I:%M:%S %p")
        print('------------------------------------------------------------------------------------------------')
        print(reg_format_date)
        print('------------------------------------------------------------------------------------------------')
        string = "[+] All Fields are Mandatory \n[+] Avoid any kind of Spelling Mistakes \n[+] Write Everything in uppercase letters \n:"

        for letter in string:
            sleep(0.01)  # In seconds
            sys.stdout.write(letter)
            sys.stdout.flush()

        # starting position of the message

        (x, y) = (50, 50)
        message = input('\nEnter Your Company \ Institute Name: ')
        company = message
        color = 'rgb(0, 0, 0)'
        font = ImageFont.truetype('arial.ttf', size=80)
        draw.text((x, y), message, fill=color, font=font)

        # adding an unique id number. You can manually take it from user
        (x, y) = (600, 75)
        idno = input("\nEnter your ID no.")
        message = str('ID ' + str(idno))
        color = 'rgb(0, 0, 0)'  # black color
        font = ImageFont.truetype('arial.ttf', size=60)
        draw.text((x, y), message, fill=color, font=font)

        (x, y) = (50, 250)
        message = input('Enter Your Full Name: ')
        name = message
        color = 'rgb(0, 0, 0)'  # black color
        font = ImageFont.truetype('arial.ttf', size=45)
        draw.text((x, y), message, fill=color, font=font)

        (x, y) = (50, 350)
        message = input('Enter Your Gender: ')
        gen = message
        color = 'rgb(0, 0, 0)'  # black color
        draw.text((x, y), message, fill=color, font=font)
        (x, y) = (250, 350)
        message = input('Enter Your Age: ')
        color = 'rgb(0, 0, 0)'  # black color
        draw.text((x, y), message, fill=color, font=font)
        age = message

        (x, y) = (50, 450)
        message = input('Enter Your Date Of Birth: ')
        color = 'rgb(0, 0, 0)'  # black color
        draw.text((x, y), message, fill=color, font=font)
        dob = message
        (x, y) = (50, 550)
        message = input('Enter Your Blood Group: ')
        color = 'rgb(255, 0, 0)'  # black color
        draw.text((x, y), message, fill=color, font=font)
        blc = message
        (x, y) = (50, 650)
        message = input('Enter Your Mobile Number: ')
        temp = message
        color = 'rgb(0, 0, 0)'  # black color
        draw.text((x, y), message, fill=color, font=font)

        (x, y) = (50, 750)
        message = input('Enter Your Address: ')
        color = 'rgb(0, 0, 0)'  # black color
        draw.text((x, y), message, fill=color, font=font)
        adr = message
        # save the edited image
        conc =  "\n Contact no. :"+ temp +"\n"+ dob + "\n Blood Group :" + blc + "\n"   + gen
        image.save(str(name) + '.png')

        img = qrcode.make(str(company) + "_"+ str(idno) + str(conc))  # this info. is added in QR code, also add other things
        img.save(str(idno) + '.bmp')

        til = Image.open(name + '.png')
        im = Image.open(str(idno) + '.bmp')  # 25x25
        til.paste(im, (500, 230))
        til.save(name + '.png')

        print(('\n\n\nYour ID Card Successfully created in a PNG file ' + name + '.png'))
        sh = input("show card ? (y/n)")
        if sh =="y":
            til.show()
        elif sh =="n":
            print("ok")

        rs3t= input("restart ? (y/n)")
        if rs3t == "y":
            restart()
        elif rs3t == "n":
            import time
            import sys

            print("Disconnecting  Console ...:")

            # animation = ["10%", "20%", "30%", "40%", "50%", "60%", "70%", "80%", "90%", "100%"]
            animation = ["[■□□□□□□□□□]", "[■■□□□□□□□□]", "[■■■□□□□□□□]", "[■■■■□□□□□□]", "[■■■■■□□□□□]", "[■■■■■■□□□□]",
                         "[■■■■■■■□□□]", "[■■■■■■■■□□]", "[■■■■■■■■■□]", "[■■■■■■■■■■]"]

            for i in range(len(animation)):
                time.sleep(0.02)
                sys.stdout.write("\r" + animation[i % len(animation)])
                sys.stdout.flush()

            print("\n")
            print("done...")

elif option =="5":
    from pyzbar import pyzbar
    import cv2

    opin30 = input("scan Qr code using Camera Vision or scan a image ?(cv/scan)")
    if opin30 == "scan":

        import pyzbar.pyzbar as pyzbar

        import cv2
        import time

        animation = ["[■□□□□□□□□□]", "[■■□□□□□□□□]", "[■■■□□□□□□□]", "[■■■■□□□□□□]", "[■■■■■□□□□□]", "[■■■■■■□□□□]",
                     "[■■■■■■■□□□]", "[■■■■■■■■□□]", "[■■■■■■■■■□]", "[■■■■■■■■■■]"]

        for i in range(len(animation)):
            time.sleep(0.04)
            sys.stdout.write("\r" + animation[i % len(animation)])
            sys.stdout.flush()

            lao = input("\nenter file name:")

            img_path = lao

            img = cv2.imread(img_path)

            barcodes = pyzbar.decode(img)

            for barcode in barcodes:
                (x, y, w, h) = barcode.rect
                cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 2)
                barcodeData = barcode.data.decode("utf-8")
                barcodeType = barcode.type
                text = "{} ({})".format(barcodeData, barcodeType)
                cv2.putText(img, text, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)
                print("[INFO] found {} barcode {}\n:".format(barcodeType, barcodeData))
            rsrt = input("restart ? (y/n)")
            if rsrt == "y":
                restart()
            elif rsrt == "n":
                import time
                import sys

                print("Disconnecting  Console ...:")

                # animation = ["10%", "20%", "30%", "40%", "50%", "60%", "70%", "80%", "90%", "100%"]
                animation = ["[■□□□□□□□□□]", "[■■□□□□□□□□]", "[■■■□□□□□□□]", "[■■■■□□□□□□]", "[■■■■■□□□□□]",
                             "[■■■■■■□□□□]",
                             "[■■■■■■■□□□]", "[■■■■■■■■□□]", "[■■■■■■■■■□]", "[■■■■■■■■■■]"]

                for i in range(len(animation)):
                    time.sleep(0.02)
                    sys.stdout.write("\r" + animation[i % len(animation)])
                    sys.stdout.flush()

                print("\n")
                print("done...")
    elif opin30 == "cv":
        import pyzbar.pyzbar as pyzbar
        import numpy as np
        import cv2
        import time

        cap = cv2.VideoCapture(0)

        cap.set(3, 640)
        cap.set(4, 480)

        # 160.0 x 120.0
        # 176.0 x 144.0
        # 320.0 x 240.0
        # 352.0 x 288.0
        # 640.0 x 480.0
        # 1024.0 x 768.0
        # 1280.0 x 1024.0
        time.sleep(2)


        def decode(im):
            decodedObjects = pyzbar.decode(im)
            # Print results
            for obj in decodedObjects:
                print('Type : ', obj.type)
                print('Data : ', obj.data, '\n')
            return decodedObjects
            # Find barcodes and QR codes


        font = cv2.FONT_HERSHEY_SIMPLEX

        while (cap.isOpened()):
            # Capture frame-by-frame
            ret, frame = cap.read()
            # Our operations on the frame come here
            im = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

            decodedObjects = decode(im)

            for decodedObject in decodedObjects:
                points = decodedObject.polygon

                # If the points do not form a quad, find convex hull
                if len(points) > 4:
                    hull = cv2.convexHull(np.array([point for point in points], dtype=np.float32))
                    hull = list(map(tuple, np.squeeze(hull)))
                else:
                    hull = points

                # Number of points in the convex hull
                n = len(hull)
                # Draw the convext hull
                for j in range(0, n):
                    cv2.line(frame, hull[j], hull[(j + 1) % n], (255, 0, 0), 3)

                x = decodedObject.rect.left
                y = decodedObject.rect.top

                print(x, y)

                print('Type : ', decodedObject.type)
                print('Data : ', decodedObject.data, '\n')

                barCode = str(decodedObject.data)
                cv2.putText(frame, barCode, (x, y), font, 1, (0, 255, 255), 2, cv2.LINE_AA)

            # Display the resulting frame
            cv2.imshow('frame', frame)
            key = cv2.waitKey(1)
            if key & 0xFF == ord('q'):
                break
            elif key & 0xFF == ord('s'):  # wait for 's' key to save
                cv2.imwrite('Capture.png', frame)

        cap.release()
        cv2.destroyAllWindows()


elif option == "6":
    # import necessary modules

    # for implementing the HTTP Web servers
    import http.server

    # provides access to the BSD socket interface
    import socket

    # a framework for network servers
    import socketserver

    # to display a Web-based documents to users
    import webbrowser

    # to generate qrcode
    import pyqrcode
    from pyqrcode import QRCode

    # convert into png format
    import png

    # to access operating system control
    import os

    # assigning the appropriate port value
    PORT = 8010
    # this finds the name of the computer user
    os.environ['USERPROFILE']

    # changing the directory to access the files desktop
    # with the help of os module
    desktop = os.path.join(os.path.join(os.environ['USERPROFILE']),
                           'OneDrive')
    os.chdir(desktop)

    # creating a http request
    Handler = http.server.SimpleHTTPRequestHandler
    # returns, host name of the system under
    # which Python interpreter is executed
    hostname = socket.gethostname()

    # finding the IP address of the PC
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    IP = "http://" + s.getsockname()[0] + ":" + str(PORT)
    link = IP

    # converting the IP address into the form of a QRcode
    # with the help of pyqrcode module

    # converts the IP address into a Qrcode
    url = pyqrcode.create(link)
    # saves the Qrcode inform of svg
    url.svg("myqr.svg", scale=8)
    # opens the Qrcode image in the web browser
    webbrowser.open('myqr.svg')

    # Creating the HTTP request and serving the
    # folder in the PORT 8010,and the pyqrcode is generated

    # continuous stream of data between client and server
    with socketserver.TCPServer(("", PORT), Handler) as httpd:
        print("serving at port", PORT)
        print("Type this in your Browser", IP)
        print("or Use the QRCode")
        httpd.serve_forever()

    rs3t = input("restart ? (y/n)")
    if rs3t == "y":
        restart()
    elif rs3t == "n":
        import time
        import sys

        print("Disconnecting  Console ...:")

        # animation = ["10%", "20%", "30%", "40%", "50%", "60%", "70%", "80%", "90%", "100%"]
        animation = ["[■□□□□□□□□□]", "[■■□□□□□□□□]", "[■■■□□□□□□□]", "[■■■■□□□□□□]", "[■■■■■□□□□□]", "[■■■■■■□□□□]",
                     "[■■■■■■■□□□]", "[■■■■■■■■□□]", "[■■■■■■■■■□]", "[■■■■■■■■■■]"]

        for i in range(len(animation)):
            time.sleep(0.02)
            sys.stdout.write("\r" + animation[i % len(animation)])
            sys.stdout.flush()

        print("\n")
        print("done...")
elif option =="7":
    from MyQR import myqr
    import os

    print("starting dynamic Console ...:")

    # animation = ["10%", "20%", "30%", "40%", "50%", "60%", "70%", "80%", "90%", "100%"]
    animation = ["[■□□□□□□□□□]", "[■■□□□□□□□□]", "[■■■□□□□□□□]", "[■■■■□□□□□□]", "[■■■■■□□□□□]", "[■■■■■■□□□□]",
                 "[■■■■■■■□□□]", "[■■■■■■■■□□]", "[■■■■■■■■■□]", "[■■■■■■■■■■]"]

    for i in range(len(animation)):
        time.sleep(0.02)
        sys.stdout.write("\r" + animation[i % len(animation)])
        sys.stdout.flush()

    string = "\na gif file is needed to create dynamic QR code\n"

    for letter in string:
        sleep(0.01)  # In seconds
        sys.stdout.write(letter)
        sys.stdout.flush()


    cl = input("colorised?(y/n)")
    if cl =="y":

        version, level, qr_name = myqr.run(

            words=input("\nenter text message or url"),
            version=6,

            level='H',

            picture=input("enter gif file name") + ".gif",

            # Color QR code
            colorized=True,
            contrast=1.0,
            brightness=1.0,
            save_name=input("save it as:") + ".gif",
            save_dir=os.getcwd()

        )
        animation = ["[■□□□□□□□□□]", "[■■□□□□□□□□]", "[■■■□□□□□□□]", "[■■■■□□□□□□]", "[■■■■■□□□□□]", "[■■■■■■□□□□]",
                     "[■■■■■■■□□□]", "[■■■■■■■■□□]", "[■■■■■■■■■□]", "[■■■■■■■■■■]"]

        for i in range(len(animation)):
            time.sleep(0.02)
            sys.stdout.write("\r" + animation[i % len(animation)])
            sys.stdout.flush()
        rs3t = input("\nrestart ? (y/n)")
        if rs3t == "y":
            restart()
        elif rs3t == "n":
            import time
            import sys

            print("Disconnecting  Console ...:")

            # animation = ["10%", "20%", "30%", "40%", "50%", "60%", "70%", "80%", "90%", "100%"]
            animation = ["[■□□□□□□□□□]", "[■■□□□□□□□□]", "[■■■□□□□□□□]", "[■■■■□□□□□□]", "[■■■■■□□□□□]", "[■■■■■■□□□□]",
                         "[■■■■■■■□□□]", "[■■■■■■■■□□]", "[■■■■■■■■■□]", "[■■■■■■■■■■]"]

            for i in range(len(animation)):
                time.sleep(0.02)
                sys.stdout.write("\r" + animation[i % len(animation)])
                sys.stdout.flush()

            print("\n")
            print("done...")
    if cl =="n":
        version, level, qr_name = myqr.run(

            words=input("\nenter text message or url"),
            version=6,

            level='H',

            picture=input("enter gif file name") + ".gif",

            # Color QR code
            colorized=False,
            contrast=1.0,
            brightness=1.0,
            save_name=input("save it as:") + ".gif",
            save_dir=os.getcwd()

        )
        animation = ["[■□□□□□□□□□]", "[■■□□□□□□□□]", "[■■■□□□□□□□]", "[■■■■□□□□□□]", "[■■■■■□□□□□]", "[■■■■■■□□□□]",
                     "[■■■■■■■□□□]", "[■■■■■■■■□□]", "[■■■■■■■■■□]", "[■■■■■■■■■■]"]

        for i in range(len(animation)):
            time.sleep(0.02)
            sys.stdout.write("\r" + animation[i % len(animation)])
            sys.stdout.flush()
        rs3t = input("\nrestart ? (y/n)")
        if rs3t == "y":
            restart()
        elif rs3t == "n":
            import time
            import sys

            print("Disconnecting  Console ...:")

            # animation = ["10%", "20%", "30%", "40%", "50%", "60%", "70%", "80%", "90%", "100%"]
            animation = ["[■□□□□□□□□□]", "[■■□□□□□□□□]", "[■■■□□□□□□□]", "[■■■■□□□□□□]", "[■■■■■□□□□□]", "[■■■■■■□□□□]",
                         "[■■■■■■■□□□]", "[■■■■■■■■□□]", "[■■■■■■■■■□]", "[■■■■■■■■■■]"]

            for i in range(len(animation)):
                time.sleep(0.02)
                sys.stdout.write("\r" + animation[i % len(animation)])
                sys.stdout.flush()

            print("\n")
            print("done...")


elif option=="ss":
    spec()
elif option == "cr":
    cr()
else :
 from colorama import Fore,Style
 print(Fore.RED+ Style.BRIGHT+"\n\n\nplease type correct option!\n\n\n\n"+Style.RESET_ALL)
 restart1()"""

from tkinter import *
import tkinter.messagebox as mb

from path import Path
from PyPDF4.pdf import PdfFileReader as PDFreader, PdfFileWriter as PDFwriter
import pyttsx3
from speech_recognition import Recognizer, AudioFile
from pydub import AudioSegment
import os


# Initializing the GUI window
class Window(Tk):
    def __init__(self):
        super(Window, self).__init__()
        self.title("R1SH4BH")
        self.geometry('400x250')
        self.resizable(0, 0)
        self.config(bg='BLACK')

        Label(self, text='R1SH4BH PROJECT', wraplength=400,
              bg='Burlywood', font=("Comic Sans MS", 15)).place(x=0, y=0)

        Button(self, text="Convert PDF to Audio", font=("Comic Sans MS", 15), bg='Tomato',
               command=self.pdf_to_audio, width=25).place(x=40, y=80)

        Button(self, text="Convert Audio to PDF", font=("Comic Sans MS", 15), bg='Tomato',
               command=self.audio_to_pdf, width=25).place(x=40, y=150)

    def pdf_to_audio(self):
        pta = Toplevel(self)
        pta.title('Convert PDF to Audio')
        pta.geometry('500x300')
        pta.resizable(0, 0)
        pta.config(bg='Chocolate')

        Label(pta, text='Convert PDF to Audio', font=('Comic Sans MS', 15), bg='Chocolate').place(relx=0.3, y=0)

        Label(pta, text='Enter the PDF file location (with extension): ', bg='Chocolate', font=("Verdana", 11)).place(
            x=10, y=60)
        filename = Entry(pta, width=32, font=('Verdana', 11))
        filename.place(x=10, y=90)

        Label(pta, text='Enter the page to read from the PDF (only one can be read): ', bg='Chocolate',
              font=("Verdana", 11)).place(x=10, y=140)
        page = Entry(pta, width=15, font=('Verdana', 11))
        page.place(x=10, y=170)

        Button(pta, text='Speak the text', font=('Gill Sans MT', 12), bg='Snow', width=20,
               command=lambda: self.speak_text(filename.get(), page.get())).place(x=150, y=240)

    def audio_to_pdf(self):
        atp = Toplevel(self)
        atp.title('Convert Audio to PDF')
        atp.geometry('675x300')
        atp.resizable(0, 0)
        atp.config(bg='FireBrick')

        Label(atp, text='Convert Audio to PDF', font=("Comic Sans MS", 15), bg='FireBrick').place(relx=0.36, y=0)

        Label(atp, text='Enter the Audio File location that you want to read [in .wav or .mp3 extensions only]:',
              bg='FireBrick', font=('Verdana', 11)).place(x=20, y=60)
        audiofile = Entry(atp, width=58, font=('Verdana', 11))
        audiofile.place(x=20, y=90)

        Label(atp, text='Enter the PDF File location that you want to save the text in (with extension):',
              bg='FireBrick', font=('Verdana', 11)).place(x=20, y=140)
        pdffile = Entry(atp, width=58, font=('Verdana', 11))
        pdffile.place(x=20, y=170)

        Button(atp, text='Create PDF', bg='Snow', font=('Gill Sans MT', 12), width=20,
               command=lambda: self.speech_recognition(audiofile.get(), pdffile.get())).place(x=247, y=230)

    @staticmethod
    def speak_text(filename, page):
        if not filename or not page:
            mb.showerror('Missing field!', 'Please check your responses, because one of the fields is missing')
            return

        reader = PDFreader(filename)
        engine = pyttsx3.init()

        with Path(filename).open('rb'):
            page_to_read = reader.getPage(int(page) - 1)
            text = page_to_read.extractText()

            engine.say(text)
            engine.runAndWait()

    @staticmethod
    def write_text(filename, text):
        writer = PDFwriter()
        writer.addBlankPage(72, 72)

        pdf_path = Path(filename)

        with pdf_path.open('ab') as output_file:
            writer.write(output_file)
            output_file.write(text)

    def speech_recognition(self, audio, pdf):
        if not audio or not pdf:
            mb.showerror('Missing field!', 'Please check your responses, because one of the fields is missing')
            return

        audio_file_name = os.path.basename(audio).split('.')[0]
        audio_file_extension = os.path.basename(audio).split('.')[1]

        if audio_file_extension != 'wav' and audio_file_extension != 'mp3':
            mb.showerror('Error!', 'The format of the audio file should only be either "wav" and "mp3"!')

        if audio_file_extension == 'mp3':
            audio_file = AudioSegment.from_file(Path(audio), format='mp3')
            audio_file.export(f'{audio_file_name}.wav', format='wav')

        source_file = f'{audio_file_name}.wav'

        r = Recognizer()
        with AudioFile(source_file) as source:
            r.pause_threshold = 5
            speech = r.record(source)

            text = r.recognize_google(speech)

            self.write_text(pdf, text)


# Finalizing the GUI window
app = Window()

app.update()
app.mainloop()