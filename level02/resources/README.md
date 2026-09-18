# Level 02

## Check what is available at level launch
```bash
ls -la
----r--r-- 1 flag02  level02 8302 Aug 30  2015 level02.pcap
# pcap file appears in the folder

cat level02.pcap
# gives unreadable symbols
```

The subject in the intra said
> It is advisable to learn how to use the scp command

```bash
scp -P 4242 level02@xx.xx.xx.xx:/home/user/level02/level02.pcap ./
# retrieve file and transfer it outside the VM
```

## Read PCAP file
After retrieving the file, you can open it in a tool that analyses network packets.  
We choose Wireshark. It's an open-source network packet analyser used to capture,
inspect and analyse data traffic. It presents them in a human-readable format.
- Move/scroll to next packet
- In the bottom right box 'Packet bytes' pane : you can see hex packets and can make out certain bits of words :
    - scroll until you see a 'Pass word:': you see the raw hex + ascii view
- You can look at the packet in detail using `Follow -> TCP Stream` which gives you the raw sequence of keystrokes typed :
    - Looking at it there's a word that looks like English but broken by certain characters
    - Switch to `Hex Dump` view for more precision about what was entered
    - Decoding it you can see there are mistakes made while typing the password
        - Removing the `7f` (DEL/Backspace) you can reconstruct the password
        - Here is the full sequence without modification :  
        `66 74 5f 77 61 6e 64 72 7f 7f 7f 4e 44 52 65 6c 7f 4c 30 4c 0d`