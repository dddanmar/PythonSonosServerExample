# Python Sonos Server Example
An example of running a Sonos SOAP Server in Python, listing and playing public Hamish and Andy podcasts.

Sonos_Soap.py was created from the WDSL file supplied by Sonos.

# To run
```pip install -r requirements.txt

python main.py```

# To connect with Sonos Speaker
Follow the instructions here http://www.hirahim.com/projects/sonos-soundcloud/

Using the following options (ignore optionals):
```SID: 255
Service Name: Hamish and Andy
Endpoint URL: http://192.168.1.1:7789
Secure Endpoint URL: http://192.168.1.1:7789
Polling interval: 300
Authentication SOAP header policy: Anonymous
Container Type: Select the “Music Service” option
```

Open the Sonos Controller App, You should now have 'Hamish and Andy' in the list of installed music services.
