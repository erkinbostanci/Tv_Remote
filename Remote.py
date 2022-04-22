import random
import time

class Remote():


    def __init__(self,tv_status = "Close",tv_volume = 0,channel_list = ["NBC"],channel = "NBC"):

        self.tv_status = tv_status

        self.tv_volume = tv_volume

        self.channel_list = channel_list

        self.channel = channel

    def tv_open(self):

        if (self.tv_status == "Open"):
            print("Tv Already Open....")
        else:
            print("Tv Opening...")
            self.tv_status  = "Open"

    def tv_close(self):

        if (self.tv_status == "Close"):
            print("Tv Already Close..")
        else:
            print("Tv Closing....")
            self.tv_status = "Close"

    def tv_sound_settings(self):

        while True:
            ent =  input("Volume Down: '<'\Volume Up : '>'\Quit : quit")

            if (ent == "<"):
                if (self.tv_volume != 0):

                    self.tv_volume -= 1
                    print("Volume:",self.tv_volume)
            elif (ent == ">"):
                if (self.tv_volume != 31):

                    self.tv_volume += 1

                    print("Volume:",self.tv_volume)
            else:
                print("Volume update:",self.tv_volume)
                break
    def channel_adding(self,channel_list):

        print("Channel Adding....")
        time.sleep(1)

        self.channel_list.append(channel_list)

        print("Channel added.....")
    def random_channel(self):

        rnd_ch = random.randint(0,len(self.channel_list)-1)

        self.channel = self.channel_list[rnd_ch]

        print("Current Channel:" ,self.channel)
    def __len__(self):

        return len(self.channel_list)

    def __str__(self):

        return "Tv Status: {}\nTv Volume: {}\nChannel List: {}\nCurrent Channel: {}\n".format(self.tv_status,self.tv_volume,self.channel_list,self.channel)


remote = Remote()


print("""
Tv APP
1. Open Tv
2. Close Tv
3. Sound Settings
4. Add Channel
5. Channel List
6. Random Channel
7. Tv Info
Press 'q' for quit
""")


while True:

    select = input("Select Transaction:")

    if (select == "q"):
        print("Closing...")
        break

    elif (select == "1"):
        remote.tv_open()
    elif (select == "2"):
        remote.tv_close()

    elif (select == "3"):
        remote.tv_sound_settings()

    elif (select == "4"):
        ch_add = input("Channel name in ',' adding :")

        channel_adding = ch_add.split(",")

        for adding in channel_adding:
            remote.channel_adding(adding)
    elif (select == "5"):

        print("Channel List:",len(remote))

    elif (select == "6"):
        remote.random_channel()
    elif (select == "7"):
        print(remote)

    else:
        print("Wrong Input......")