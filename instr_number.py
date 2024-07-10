import re

def extract_cpi(report):

    exec_blocks = re.findall(r"EXEC NAME: (.+?)\n.*?Real instructions: (\d+)", report, re.DOTALL)

    for exec_name,  instructions in exec_blocks:

        instructions = int(instructions)


      


        print(f"{exec_name}: instr number = {instructions}")


report_data = """
EXEC NAME: aha-mont64
[1;32mTEST REPORT: SUCCESS.[0m
Real cycles: 6078215
Real instructions: 4531262
BOOT file: /home/mrabiai/Bureau/herd-ware/sw/embench-iot/hex/SIM/WAESP32AU1V010F/aha-mont64.boot8.hex
iROM file: /home/mrabiai/Bureau/herd-ware/sw/embench-iot/hex/SIM/WAESP32AU1V010F/aha-mont64.irom8.hex
Simulation fast clock cycles (/1): 12185980
Simulation main clock cycles (/2): 6092990

------------------------------
           HART: 0
------------------------------
Cycles: 6092985
Time: 6092985
Retired instructions: 4542232
ALU instructions: 4040578
BRU instructions: 466014
MUL instructions: 35632
DIV instructions: 0
Load instructions: 9383
Store instructions: 3042
BR instructions: 460050
BR forward instructions: 257800
BR backward instructions: 202250
JAL instructions: 4679
JALR instructions: 1285
CALL instructions: 1284
RET instructions: 1285
Read cycle instructions: 2
Cache flush instructions: 0
16-bit instructions: 0
32-bit instructions: 4542232
0 read port: 4702
1 read port: 2410169
2 read port: 2127361
Taken BR: 354464
Taken BR forward: 167057
Taken BR backward: 187407
Not taken BR: 105586
Not taken BR forward: 90743
Not taken BR backward: 14843
Mispredicted instructions: 360428
Mispredicted BR: 354464
Mispredicted BR taken: 354464
Mispredicted BR forward taken: 167057
Mispredicted BR backward taken: 187407
Mispredicted BR not taken: 0
Mispredicted BR forward not taken: 0
Mispredicted BR backward not taken: 0
Mispredicted JALR: 1285
Mispredicted CALL: 1284
Mispredicted RET: 1285
Partial instructions: 0
Instruction buffer full: 0
Instruction buffer dead: 0
Wait source dependency: 2984
Wait MUL unit: 106896
Wait DIV unit: 0
Wait data request: 430
Wait data acknowledgement: 438
Empty buffer for misaligned instructions: 0
Empty fetch port: 720858
Empty commit port: 1550753
L1I hits: 0
L1I misses: 0
L1I prefetches: 0
L1D hits: 0
L1D misses: 0
L1D prefetches: 0
L2 hits: 0
L2 misses: 0
L2 prefetches: 0
------------------------------

EXEC NAME: crc32
[1;31mTEST REPORT: FAILED.[0m
Real cycles: 6791555
Real instructions: 3831161
BOOT file: /home/mrabiai/Bureau/herd-ware/sw/embench-iot/hex/SIM/WAESP32AU1V010F/crc32.boot8.hex
iROM file: /home/mrabiai/Bureau/herd-ware/sw/embench-iot/hex/SIM/WAESP32AU1V010F/crc32.irom8.hex
Simulation fast clock cycles (/1): 13663646
Simulation main clock cycles (/2): 6831823

------------------------------
           HART: 0
------------------------------
Cycles: 6831818
Time: 6831818
Retired instructions: 3853898
ALU instructions: 3152923
BRU instructions: 525863
MUL instructions: 175104
DIV instructions: 0
Load instructions: 350231
Store instructions: 175315
BR instructions: 175285
BR forward instructions: 8
BR backward instructions: 175277
JAL instructions: 175290
JALR instructions: 175288
CALL instructions: 175287
RET instructions: 175288
Read cycle instructions: 2
Cache flush instructions: 0
16-bit instructions: 0
32-bit instructions: 3853898
0 read port: 525519
1 read port: 2102229
2 read port: 1226150
Taken BR: 175104
Taken BR forward: 1
Taken BR backward: 175103
Not taken BR: 181
Not taken BR forward: 7
Not taken BR backward: 174
Mispredicted instructions: 525682
Mispredicted BR: 175104
Mispredicted BR taken: 175104
Mispredicted BR forward taken: 1
Mispredicted BR backward taken: 175103
Mispredicted BR not taken: 0
Mispredicted BR forward not taken: 0
Mispredicted BR backward not taken: 0
Mispredicted JALR: 175288
Mispredicted CALL: 175287
Mispredicted RET: 175288
Partial instructions: 0
Instruction buffer full: 0
Instruction buffer dead: 0
Wait source dependency: 350219
Wait MUL unit: 524970
Wait DIV unit: 0
Wait data request: 0
Wait data acknowledgement: 4
Empty buffer for misaligned instructions: 0
Empty fetch port: 1051365
Empty commit port: 2977920
L1I hits: 0
L1I misses: 0
L1I prefetches: 0
L1D hits: 0
L1D misses: 0
L1D prefetches: 0
L2 hits: 0
L2 misses: 0
L2 prefetches: 0
------------------------------

EXEC NAME: cubic
[1;31mTEST REPORT: FAILED.[0m
Real cycles: 10089630
Real instructions: 6637287
BOOT file: /home/mrabiai/Bureau/herd-ware/sw/embench-iot/hex/SIM/WAESP32AU1V010F/cubic.boot8.hex
iROM file: /home/mrabiai/Bureau/herd-ware/sw/embench-iot/hex/SIM/WAESP32AU1V010F/cubic.irom8.hex
Simulation fast clock cycles (/1): 22199084
Simulation main clock cycles (/2): 11099542

------------------------------
           HART: 0
------------------------------
Cycles: 11099537
Time: 11099537
Retired instructions: 7301680
ALU instructions: 6028005
BRU instructions: 889833
MUL instructions: 353914
DIV instructions: 24882
Load instructions: 647812
Store instructions: 596770
BR instructions: 734341
BR forward instructions: 593699
BR backward instructions: 140642
JAL instructions: 111049
JALR instructions: 44443
CALL instructions: 44122
RET instructions: 44123
Read cycle instructions: 2
Cache flush instructions: 0
16-bit instructions: 0
32-bit instructions: 7301680
0 read port: 318774
1 read port: 3289202
2 read port: 3693704
Taken BR: 376139
Taken BR forward: 287994
Taken BR backward: 88145
Not taken BR: 358202
Not taken BR forward: 305705
Not taken BR backward: 52497
Mispredicted instructions: 531631
Mispredicted BR: 376139
Mispredicted BR taken: 376139
Mispredicted BR forward taken: 287994
Mispredicted BR backward taken: 88145
Mispredicted BR not taken: 0
Mispredicted BR forward not taken: 0
Mispredicted BR backward not taken: 0
Mispredicted JALR: 44443
Mispredicted CALL: 44122
Mispredicted RET: 44123
Partial instructions: 0
Instruction buffer full: 0
Instruction buffer dead: 23760
Wait source dependency: 457579
Wait MUL unit: 726550
Wait DIV unit: 561616
Wait data request: 43978
Wait data acknowledgement: 108070
Empty buffer for misaligned instructions: 0
Empty fetch port: 1081622
Empty commit port: 3797857
L1I hits: 0
L1I misses: 0
L1I prefetches: 0
L1D hits: 0
L1D misses: 0
L1D prefetches: 0
L2 hits: 0
L2 misses: 0
L2 prefetches: 0
------------------------------

EXEC NAME: edn
[1;31mTEST REPORT: FAILED.[0m
Real cycles: 6842548
Real instructions: 3919331
BOOT file: /home/mrabiai/Bureau/herd-ware/sw/embench-iot/hex/SIM/WAESP32AU1V010F/edn.boot8.hex
iROM file: /home/mrabiai/Bureau/herd-ware/sw/embench-iot/hex/SIM/WAESP32AU1V010F/edn.irom8.hex
Simulation fast clock cycles (/1): 13846702
Simulation main clock cycles (/2): 6923351

------------------------------
           HART: 0
------------------------------
Cycles: 6923346
Time: 6923346
Retired instructions: 3965791
ALU instructions: 2183319
BRU instructions: 360206
MUL instructions: 580008
DIV instructions: 0
Load instructions: 1330979
Store instructions: 111105
BR instructions: 359381
BR forward instructions: 187
BR backward instructions: 359194
JAL instructions: 459
JALR instructions: 366
CALL instructions: 365
RET instructions: 366
Read cycle instructions: 2
Cache flush instructions: 0
16-bit instructions: 0
32-bit instructions: 3965791
0 read port: 569
1 read port: 2245984
2 read port: 1719238
Taken BR: 348102
Taken BR forward: 90
Taken BR backward: 348012
Not taken BR: 11279
Not taken BR forward: 97
Not taken BR backward: 11182
Mispredicted instructions: 348927
Mispredicted BR: 348102
Mispredicted BR taken: 348102
Mispredicted BR forward taken: 90
Mispredicted BR backward taken: 348012
Mispredicted BR not taken: 0
Mispredicted BR forward not taken: 0
Mispredicted BR backward not taken: 0
Mispredicted JALR: 366
Mispredicted CALL: 365
Mispredicted RET: 366
Partial instructions: 0
Instruction buffer full: 0
Instruction buffer dead: 0
Wait source dependency: 1032437
Wait MUL unit: 1605384
Wait DIV unit: 0
Wait data request: 7392
Wait data acknowledgement: 8982
Empty buffer for misaligned instructions: 0
Empty fetch port: 697855
Empty commit port: 2957555
L1I hits: 0
L1I misses: 0
L1I prefetches: 0
L1D hits: 0
L1D misses: 0
L1D prefetches: 0
L2 hits: 0
L2 misses: 0
L2 prefetches: 0
------------------------------

EXEC NAME: huffbench
[1;32mTEST REPORT: SUCCESS.[0m
Real cycles: 4332796
Real instructions: 2598467
BOOT file: /home/mrabiai/Bureau/herd-ware/sw/embench-iot/hex/SIM/WAESP32AU1V010F/huffbench.boot8.hex
iROM file: /home/mrabiai/Bureau/herd-ware/sw/embench-iot/hex/SIM/WAESP32AU1V010F/huffbench.irom8.hex
Simulation fast clock cycles (/1): 9473252
Simulation main clock cycles (/2): 4736626

------------------------------
           HART: 0
------------------------------
Cycles: 4736621
Time: 4736621
Retired instructions: 2840278
ALU instructions: 2080856
BRU instructions: 598002
MUL instructions: 0
DIV instructions: 0
Load instructions: 665991
Store instructions: 200954
BR instructions: 545278
BR forward instructions: 270071
BR backward instructions: 275207
JAL instructions: 51449
JALR instructions: 1275
CALL instructions: 1261
RET instructions: 1262
Read cycle instructions: 2
Cache flush instructions: 0
16-bit instructions: 0
32-bit instructions: 2840278
0 read port: 54331
1 read port: 1792530
2 read port: 993417
Taken BR: 310595
Taken BR forward: 60364
Taken BR backward: 250231
Not taken BR: 234683
Not taken BR forward: 209707
Not taken BR backward: 24976
Mispredicted instructions: 363319
Mispredicted BR: 310595
Mispredicted BR taken: 310595
Mispredicted BR forward taken: 60364
Mispredicted BR backward taken: 250231
Mispredicted BR not taken: 0
Mispredicted BR forward not taken: 0
Mispredicted BR backward not taken: 0
Mispredicted JALR: 1275
Mispredicted CALL: 1261
Mispredicted RET: 1262
Partial instructions: 0
Instruction buffer full: 0
Instruction buffer dead: 125
Wait source dependency: 597732
Wait MUL unit: 0
Wait DIV unit: 0
Wait data request: 384
Wait data acknowledgement: 1263
Empty buffer for misaligned instructions: 0
Empty fetch port: 726764
Empty commit port: 1896343
L1I hits: 0
L1I misses: 0
L1I prefetches: 0
L1D hits: 0
L1D misses: 0
L1D prefetches: 0
L2 hits: 0
L2 misses: 0
L2 prefetches: 0
------------------------------

EXEC NAME: matmult-int
[1;32mTEST REPORT: SUCCESS.[0m
Real cycles: 6163938
Real instructions: 3183124
BOOT file: /home/mrabiai/Bureau/herd-ware/sw/embench-iot/hex/SIM/WAESP32AU1V010F/matmult-int.boot8.hex
iROM file: /home/mrabiai/Bureau/herd-ware/sw/embench-iot/hex/SIM/WAESP32AU1V010F/matmult-int.irom8.hex
Simulation fast clock cycles (/1): 12675370
Simulation main clock cycles (/2): 6337685

------------------------------
           HART: 0
------------------------------
Cycles: 6337680
Time: 6337680
Retired instructions: 3266800
ALU instructions: 2482427
BRU instructions: 407565
MUL instructions: 376000
DIV instructions: 800
Load instructions: 790836
Store instructions: 435654
BR instructions: 407440
BR forward instructions: 411
BR backward instructions: 407029
JAL instructions: 64
JALR instructions: 61
CALL instructions: 60
RET instructions: 61
Read cycle instructions: 2
Cache flush instructions: 0
16-bit instructions: 0
32-bit instructions: 3266800
0 read port: 104
1 read port: 1667292
2 read port: 1599404
Taken BR: 387105
Taken BR forward: 3
Taken BR backward: 387102
Not taken BR: 20335
Not taken BR forward: 408
Not taken BR backward: 19927
Mispredicted instructions: 387230
Mispredicted BR: 387105
Mispredicted BR taken: 387105
Mispredicted BR forward taken: 3
Mispredicted BR backward taken: 387102
Mispredicted BR not taken: 0
Mispredicted BR forward not taken: 0
Mispredicted BR backward not taken: 0
Mispredicted JALR: 61
Mispredicted CALL: 60
Mispredicted RET: 61
Partial instructions: 0
Instruction buffer full: 0
Instruction buffer dead: 800
Wait source dependency: 1505212
Wait MUL unit: 1128000
Wait DIV unit: 15945
Wait data request: 0
Wait data acknowledgement: 4
Empty buffer for misaligned instructions: 0
Empty fetch port: 775261
Empty commit port: 3070880
L1I hits: 0
L1I misses: 0
L1I prefetches: 0
L1D hits: 0
L1D misses: 0
L1D prefetches: 0
L2 hits: 0
L2 misses: 0
L2 prefetches: 0
------------------------------

EXEC NAME: md5sum
[1;32mTEST REPORT: SUCCESS.[0m
Real cycles: 2761663
Real instructions: 2046782
BOOT file: /home/mrabiai/Bureau/herd-ware/sw/embench-iot/hex/SIM/WAESP32AU1V010F/md5sum.boot8.hex
iROM file: /home/mrabiai/Bureau/herd-ware/sw/embench-iot/hex/SIM/WAESP32AU1V010F/md5sum.irom8.hex
Simulation fast clock cycles (/1): 5639194
Simulation main clock cycles (/2): 2819597

------------------------------
           HART: 0
------------------------------
Cycles: 2819592
Time: 2819592
Retired instructions: 2089516
ALU instructions: 1814376
BRU instructions: 275080
MUL instructions: 52
DIV instructions: 0
Load instructions: 181996
Store instructions: 89277
BR instructions: 234179
BR forward instructions: 121643
BR backward instructions: 112536
JAL instructions: 40419
JALR instructions: 482
CALL instructions: 428
RET instructions: 429
Read cycle instructions: 2
Cache flush instructions: 0
16-bit instructions: 0
32-bit instructions: 2089516
0 read port: 41491
1 read port: 921342
2 read port: 1126683
Taken BR: 128030
Taken BR forward: 28394
Taken BR backward: 99636
Not taken BR: 106149
Not taken BR forward: 93249
Not taken BR backward: 12900
Mispredicted instructions: 168931
Mispredicted BR: 128030
Mispredicted BR taken: 128030
Mispredicted BR forward taken: 28394
Mispredicted BR backward taken: 99636
Mispredicted BR not taken: 0
Mispredicted BR forward not taken: 0
Mispredicted BR backward not taken: 0
Mispredicted JALR: 482
Mispredicted CALL: 428
Mispredicted RET: 429
Partial instructions: 0
Instruction buffer full: 0
Instruction buffer dead: 0
Wait source dependency: 54193
Wait MUL unit: 156
Wait DIV unit: 0
Wait data request: 104
Wait data acknowledgement: 160
Empty buffer for misaligned instructions: 0
Empty fetch port: 337863
Empty commit port: 730076
L1I hits: 0
L1I misses: 0
L1I prefetches: 0
L1D hits: 0
L1D misses: 0
L1D prefetches: 0
L2 hits: 0
L2 misses: 0
L2 prefetches: 0
------------------------------

EXEC NAME: minver
[1;31mTEST REPORT: FAILED.[0m
Real cycles: 8208550
Real instructions: 4964001
BOOT file: /home/mrabiai/Bureau/herd-ware/sw/embench-iot/hex/SIM/WAESP32AU1V010F/minver.boot8.hex
iROM file: /home/mrabiai/Bureau/herd-ware/sw/embench-iot/hex/SIM/WAESP32AU1V010F/minver.irom8.hex
Simulation fast clock cycles (/1): 16448112
Simulation main clock cycles (/2): 8224056

------------------------------
           HART: 0
------------------------------
Cycles: 8224051
Time: 8224051
Retired instructions: 4973403
ALU instructions: 3934154
BRU instructions: 928040
MUL instructions: 73392
DIV instructions: 35584
Load instructions: 422641
Store instructions: 385418
BR instructions: 722282
BR forward instructions: 638869
BR backward instructions: 83413
JAL instructions: 137909
JALR instructions: 67849
CALL instructions: 67292
RET instructions: 67293
Read cycle instructions: 2
Cache flush instructions: 0
16-bit instructions: 0
32-bit instructions: 4973403
0 read port: 296961
1 read port: 2761934
2 read port: 1914508
Taken BR: 321946
Taken BR forward: 279128
Taken BR backward: 42818
Not taken BR: 400336
Not taken BR forward: 359741
Not taken BR backward: 40595
Mispredicted instructions: 527704
Mispredicted BR: 321946
Mispredicted BR taken: 321946
Mispredicted BR forward taken: 279128
Mispredicted BR backward taken: 42818
Mispredicted BR not taken: 0
Mispredicted BR forward not taken: 0
Mispredicted BR backward not taken: 0
Mispredicted JALR: 67849
Mispredicted CALL: 67292
Mispredicted RET: 67293
Partial instructions: 0
Instruction buffer full: 0
Instruction buffer dead: 32805
Wait source dependency: 146256
Wait MUL unit: 132328
Wait DIV unit: 880704
Wait data request: 1668
Wait data acknowledgement: 27259
Empty buffer for misaligned instructions: 0
Empty fetch port: 1082102
Empty commit port: 3250648
L1I hits: 0
L1I misses: 0
L1I prefetches: 0
L1D hits: 0
L1D misses: 0
L1D prefetches: 0
L2 hits: 0
L2 misses: 0
L2 prefetches: 0
------------------------------

EXEC NAME: nbody
[1;31mTEST REPORT: FAILED.[0m
Real cycles: 5311374
Real instructions: 3478653
BOOT file: /home/mrabiai/Bureau/herd-ware/sw/embench-iot/hex/SIM/WAESP32AU1V010F/nbody.boot8.hex
iROM file: /home/mrabiai/Bureau/herd-ware/sw/embench-iot/hex/SIM/WAESP32AU1V010F/nbody.irom8.hex
Simulation fast clock cycles (/1): 21243874
Simulation main clock cycles (/2): 10621937

------------------------------
           HART: 0
------------------------------
Cycles: 10621932
Time: 10621932
Retired instructions: 6957245
ALU instructions: 5597396
BRU instructions: 1107265
MUL instructions: 232756
DIV instructions: 16216
Load instructions: 347265
Store instructions: 277251
BR instructions: 939104
BR forward instructions: 713393
BR backward instructions: 225711
JAL instructions: 118046
JALR instructions: 50115
CALL instructions: 50110
RET instructions: 50111
Read cycle instructions: 2
Cache flush instructions: 0
16-bit instructions: 0
32-bit instructions: 6957245
0 read port: 291071
1 read port: 3388207
2 read port: 3277967
Taken BR: 448944
Taken BR forward: 299671
Taken BR backward: 149273
Not taken BR: 490160
Not taken BR forward: 413722
Not taken BR backward: 76438
Mispredicted instructions: 617105
Mispredicted BR: 448944
Mispredicted BR taken: 448944
Mispredicted BR forward taken: 299671
Mispredicted BR backward taken: 149273
Mispredicted BR not taken: 0
Mispredicted BR forward not taken: 0
Mispredicted BR backward not taken: 0
Mispredicted JALR: 50115
Mispredicted CALL: 50110
Mispredicted RET: 50111
Partial instructions: 0
Instruction buffer full: 0
Instruction buffer dead: 19823
Wait source dependency: 119342
Wait MUL unit: 674268
Wait DIV unit: 480422
Wait data request: 0
Wait data acknowledgement: 25253
Empty buffer for misaligned instructions: 0
Empty fetch port: 1252007
Empty commit port: 3664687
L1I hits: 0
L1I misses: 0
L1I prefetches: 0
L1D hits: 0
L1D misses: 0
L1D prefetches: 0
L2 hits: 0
L2 misses: 0
L2 prefetches: 0
------------------------------

EXEC NAME: nettle-aes
[1;32mTEST REPORT: SUCCESS.[0m
Real cycles: 4714311
Real instructions: 4427412
BOOT file: /home/mrabiai/Bureau/herd-ware/sw/embench-iot/hex/SIM/WAESP32AU1V010F/nettle-aes.boot8.hex
iROM file: /home/mrabiai/Bureau/herd-ware/sw/embench-iot/hex/SIM/WAESP32AU1V010F/nettle-aes.irom8.hex
Simulation fast clock cycles (/1): 9564368
Simulation main clock cycles (/2): 4782184

------------------------------
           HART: 0
------------------------------
Cycles: 4782179
Time: 4782179
Retired instructions: 4490044
ALU instructions: 4306588
BRU instructions: 78934
MUL instructions: 0
DIV instructions: 8216
Load instructions: 840830
Store instructions: 61824
BR instructions: 77878
BR forward instructions: 10522
BR backward instructions: 67356
JAL instructions: 647
JALR instructions: 409
CALL instructions: 407
RET instructions: 408
Read cycle instructions: 2
Cache flush instructions: 0
16-bit instructions: 0
32-bit instructions: 4490044
0 read port: 2087
1 read port: 3076106
2 read port: 1411851
Taken BR: 48867
Taken BR forward: 239
Taken BR backward: 48628
Not taken BR: 29011
Not taken BR forward: 10283
Not taken BR backward: 18728
Mispredicted instructions: 53715
Mispredicted BR: 52659
Mispredicted BR taken: 48867
Mispredicted BR forward taken: 239
Mispredicted BR backward taken: 48628
Mispredicted BR not taken: 3792
Mispredicted BR forward not taken: 0
Mispredicted BR backward not taken: 3792
Mispredicted JALR: 409
Mispredicted CALL: 407
Mispredicted RET: 408
Partial instructions: 0
Instruction buffer full: 0
Instruction buffer dead: 4424
Wait source dependency: 69154
Wait MUL unit: 0
Wait DIV unit: 52456
Wait data request: 9480
Wait data acknowledgement: 8378
Empty buffer for misaligned instructions: 0
Empty fetch port: 115647
Empty commit port: 292135
L1I hits: 0
L1I misses: 0
L1I prefetches: 0
L1D hits: 0
L1D misses: 0
L1D prefetches: 0
L2 hits: 0
L2 misses: 0
L2 prefetches: 0
------------------------------

EXEC NAME: nettle-sha256
[1;32mTEST REPORT: SUCCESS.[0m
Real cycles: 4253700
Real instructions: 4015235
BOOT file: /home/mrabiai/Bureau/herd-ware/sw/embench-iot/hex/SIM/WAESP32AU1V010F/nettle-sha256.boot8.hex
iROM file: /home/mrabiai/Bureau/herd-ware/sw/embench-iot/hex/SIM/WAESP32AU1V010F/nettle-sha256.irom8.hex
Simulation fast clock cycles (/1): 8527332
Simulation main clock cycles (/2): 4263666

------------------------------
           HART: 0
------------------------------
Cycles: 4263661
Time: 4263661
Retired instructions: 4024402
ALU instructions: 3907666
BRU instructions: 48168
MUL instructions: 0
DIV instructions: 0
Load instructions: 422386
Store instructions: 155415
BR instructions: 38619
BR forward instructions: 8583
BR backward instructions: 30036
JAL instructions: 5727
JALR instructions: 3822
CALL instructions: 3344
RET instructions: 3345
Read cycle instructions: 2
Cache flush instructions: 0
16-bit instructions: 0
32-bit instructions: 4024402
0 read port: 8122
1 read port: 1790609
2 read port: 2225671
Taken BR: 27175
Taken BR forward: 3333
Taken BR backward: 23842
Not taken BR: 11444
Not taken BR forward: 5250
Not taken BR backward: 6194
Mispredicted instructions: 36724
Mispredicted BR: 27175
Mispredicted BR taken: 27175
Mispredicted BR forward taken: 3333
Mispredicted BR backward taken: 23842
Mispredicted BR not taken: 0
Mispredicted BR forward not taken: 0
Mispredicted BR backward not taken: 0
Mispredicted JALR: 3822
Mispredicted CALL: 3344
Mispredicted RET: 3345
Partial instructions: 0
Instruction buffer full: 0
Instruction buffer dead: 0
Wait source dependency: 98080
Wait MUL unit: 0
Wait DIV unit: 0
Wait data request: 6664
Wait data acknowledgement: 25708
Empty buffer for misaligned instructions: 0
Empty fetch port: 73449
Empty commit port: 239259
L1I hits: 0
L1I misses: 0
L1I prefetches: 0
L1D hits: 0
L1D misses: 0
L1D prefetches: 0
L2 hits: 0
L2 misses: 0
L2 prefetches: 0
------------------------------

EXEC NAME: nsichneu
[1;32mTEST REPORT: SUCCESS.[0m
Real cycles: 6231373
Real instructions: 2236759
BOOT file: /home/mrabiai/Bureau/herd-ware/sw/embench-iot/hex/SIM/WAESP32AU1V010F/nsichneu.boot8.hex
iROM file: /home/mrabiai/Bureau/herd-ware/sw/embench-iot/hex/SIM/WAESP32AU1V010F/nsichneu.irom8.hex
Simulation fast clock cycles (/1): 12474042
Simulation main clock cycles (/2): 6237021

------------------------------
           HART: 0
------------------------------
Cycles: 6237016
Time: 6237016
Retired instructions: 2238948
ALU instructions: 1232319
BRU instructions: 1006621
MUL instructions: 0
DIV instructions: 0
Load instructions: 1227119
Store instructions: 3759
BR instructions: 770048
BR forward instructions: 694867
BR backward instructions: 75181
JAL instructions: 236559
JALR instructions: 14
CALL instructions: 12
RET instructions: 13
Read cycle instructions: 2
Cache flush instructions: 0
16-bit instructions: 0
32-bit instructions: 2238948
0 read port: 236577
1 read port: 1228520
2 read port: 773851
Taken BR: 186047
Taken BR forward: 147843
Taken BR backward: 38204
Not taken BR: 584001
Not taken BR forward: 547024
Not taken BR backward: 36977
Mispredicted instructions: 422620
Mispredicted BR: 186047
Mispredicted BR taken: 186047
Mispredicted BR forward taken: 147843
Mispredicted BR backward taken: 38204
Mispredicted BR not taken: 0
Mispredicted BR forward not taken: 0
Mispredicted BR backward not taken: 0
Mispredicted JALR: 14
Mispredicted CALL: 12
Mispredicted RET: 13
Partial instructions: 0
Instruction buffer full: 0
Instruction buffer dead: 0
Wait source dependency: 2307585
Wait MUL unit: 0
Wait DIV unit: 0
Wait data request: 0
Wait data acknowledgement: 1236
Empty buffer for misaligned instructions: 0
Empty fetch port: 845241
Empty commit port: 3998068
L1I hits: 0
L1I misses: 0
L1I prefetches: 0
L1D hits: 0
L1D misses: 0
L1D prefetches: 0
L2 hits: 0
L2 misses: 0
L2 prefetches: 0
------------------------------

EXEC NAME: picojpeg
[1;31mTEST REPORT: FAILED.[0m
Real cycles: 5911074
Real instructions: 4134861
BOOT file: /home/mrabiai/Bureau/herd-ware/sw/embench-iot/hex/SIM/WAESP32AU1V010F/picojpeg.boot8.hex
iROM file: /home/mrabiai/Bureau/herd-ware/sw/embench-iot/hex/SIM/WAESP32AU1V010F/picojpeg.irom8.hex
Simulation fast clock cycles (/1): 13796342
Simulation main clock cycles (/2): 6898171

------------------------------
           HART: 0
------------------------------
Cycles: 6898166
Time: 6898166
Retired instructions: 4825145
ALU instructions: 3726906
BRU instructions: 478876
MUL instructions: 123116
DIV instructions: 0
Load instructions: 998427
Store instructions: 581925
BR instructions: 401444
BR forward instructions: 218735
BR backward instructions: 182709
JAL instructions: 51770
JALR instructions: 25662
CALL instructions: 24464
RET instructions: 24465
Read cycle instructions: 2
Cache flush instructions: 0
16-bit instructions: 0
32-bit instructions: 4825145
0 read port: 65911
1 read port: 3051571
2 read port: 1707663
Taken BR: 305409
Taken BR forward: 141661
Taken BR backward: 163748
Not taken BR: 96035
Not taken BR forward: 77074
Not taken BR backward: 18961
Mispredicted instructions: 382841
Mispredicted BR: 305409
Mispredicted BR taken: 305409
Mispredicted BR forward taken: 141661
Mispredicted BR backward taken: 163748
Mispredicted BR not taken: 0
Mispredicted BR forward not taken: 0
Mispredicted BR backward not taken: 0
Mispredicted JALR: 25662
Mispredicted CALL: 24464
Mispredicted RET: 24465
Partial instructions: 0
Instruction buffer full: 0
Instruction buffer dead: 5456
Wait source dependency: 431516
Wait MUL unit: 361522
Wait DIV unit: 0
Wait data request: 101437
Wait data acknowledgement: 76507
Empty buffer for misaligned instructions: 0
Empty fetch port: 771174
Empty commit port: 2073021
L1I hits: 0
L1I misses: 0
L1I prefetches: 0
L1D hits: 0
L1D misses: 0
L1D prefetches: 0
L2 hits: 0
L2 misses: 0
L2 prefetches: 0
------------------------------

EXEC NAME: primecount
[1;32mTEST REPORT: SUCCESS.[0m
Real cycles: 5013401
Real instructions: 2148524
BOOT file: /home/mrabiai/Bureau/herd-ware/sw/embench-iot/hex/SIM/WAESP32AU1V010F/primecount.boot8.hex
iROM file: /home/mrabiai/Bureau/herd-ware/sw/embench-iot/hex/SIM/WAESP32AU1V010F/primecount.irom8.hex
Simulation fast clock cycles (/1): 20054130
Simulation main clock cycles (/2): 10027065

------------------------------
           HART: 0
------------------------------
Cycles: 10027060
Time: 10027060
Retired instructions: 4297208
ALU instructions: 2339336
BRU instructions: 1826348
MUL instructions: 131516
DIV instructions: 0
Load instructions: 751215
Store instructions: 119748
BR instructions: 1760420
BR forward instructions: 1261752
BR backward instructions: 498668
JAL instructions: 65913
JALR instructions: 15
CALL instructions: 14
RET instructions: 15
Read cycle instructions: 2
Cache flush instructions: 0
16-bit instructions: 0
32-bit instructions: 4297208
0 read port: 65932
1 read port: 2099926
2 read port: 2131350
Taken BR: 704496
Taken BR forward: 325379
Taken BR backward: 379117
Not taken BR: 1055924
Not taken BR forward: 936373
Not taken BR backward: 119551
Mispredicted instructions: 770424
Mispredicted BR: 704496
Mispredicted BR taken: 704496
Mispredicted BR forward taken: 325379
Mispredicted BR backward taken: 379117
Mispredicted BR not taken: 0
Mispredicted BR forward not taken: 0
Mispredicted BR backward not taken: 0
Mispredicted JALR: 15
Mispredicted CALL: 14
Mispredicted RET: 15
Partial instructions: 0
Instruction buffer full: 0
Instruction buffer dead: 0
Wait source dependency: 2451299
Wait MUL unit: 394548
Wait DIV unit: 0
Wait data request: 0
Wait data acknowledgement: 4
Empty buffer for misaligned instructions: 0
Empty fetch port: 1540849
Empty commit port: 5729852
L1I hits: 0
L1I misses: 0
L1I prefetches: 0
L1D hits: 0
L1D misses: 0
L1D prefetches: 0
L2 hits: 0
L2 misses: 0
L2 prefetches: 0
------------------------------

EXEC NAME: qrduino
[1;31mTEST REPORT: FAILED.[0m
Real cycles: 4664704
Real instructions: 3168775
BOOT file: /home/mrabiai/Bureau/herd-ware/sw/embench-iot/hex/SIM/WAESP32AU1V010F/qrduino.boot8.hex
iROM file: /home/mrabiai/Bureau/herd-ware/sw/embench-iot/hex/SIM/WAESP32AU1V010F/qrduino.irom8.hex
Simulation fast clock cycles (/1): 11209376
Simulation main clock cycles (/2): 5604688

------------------------------
           HART: 0
------------------------------
Cycles: 5604683
Time: 5604683
Retired instructions: 3807088
ALU instructions: 2766149
BRU instructions: 505674
MUL instructions: 93792
DIV instructions: 0
Load instructions: 1031330
Store instructions: 83230
BR instructions: 473876
BR forward instructions: 221070
BR backward instructions: 252806
JAL instructions: 29053
JALR instructions: 2745
CALL instructions: 2665
RET instructions: 2666
Read cycle instructions: 2
Cache flush instructions: 0
16-bit instructions: 0
32-bit instructions: 3807088
0 read port: 32396
1 read port: 2366703
2 read port: 1407989
Taken BR: 259534
Taken BR forward: 87002
Taken BR backward: 172532
Not taken BR: 214342
Not taken BR forward: 134068
Not taken BR backward: 80274
Mispredicted instructions: 291356
Mispredicted BR: 259558
Mispredicted BR taken: 259534
Mispredicted BR forward taken: 87002
Mispredicted BR backward taken: 172532
Mispredicted BR not taken: 24
Mispredicted BR forward not taken: 18
Mispredicted BR backward not taken: 6
Mispredicted JALR: 2745
Mispredicted CALL: 2665
Mispredicted RET: 2666
Partial instructions: 0
Instruction buffer full: 0
Instruction buffer dead: 852
Wait source dependency: 707602
Wait MUL unit: 275628
Wait DIV unit: 0
Wait data request: 29562
Wait data acknowledgement: 79888
Empty buffer for misaligned instructions: 0
Empty fetch port: 583565
Empty commit port: 1797595
L1I hits: 0
L1I misses: 0
L1I prefetches: 0
L1D hits: 0
L1D misses: 0
L1D prefetches: 0
L2 hits: 0
L2 misses: 0
L2 prefetches: 0
------------------------------

EXEC NAME: sglib-combined
[1;32mTEST REPORT: SUCCESS.[0m
Real cycles: 4873677
Real instructions: 2622218
BOOT file: /home/mrabiai/Bureau/herd-ware/sw/embench-iot/hex/SIM/WAESP32AU1V010F/sglib-combined.boot8.hex
iROM file: /home/mrabiai/Bureau/herd-ware/sw/embench-iot/hex/SIM/WAESP32AU1V010F/sglib-combined.irom8.hex
Simulation fast clock cycles (/1): 10119074
Simulation main clock cycles (/2): 5059537

------------------------------
           HART: 0
------------------------------
Cycles: 5059532
Time: 5059532
Retired instructions: 2720387
ALU instructions: 1941417
BRU instructions: 681422
MUL instructions: 0
DIV instructions: 9100
Load instructions: 734387
Store instructions: 322590
BR instructions: 549478
BR forward instructions: 307281
BR backward instructions: 242197
JAL instructions: 93888
JALR instructions: 38056
CALL instructions: 38054
RET instructions: 38055
Read cycle instructions: 2
Cache flush instructions: 0
16-bit instructions: 0
32-bit instructions: 2720387
0 read port: 121074
1 read port: 1517562
2 read port: 1081751
Taken BR: 223815
Taken BR forward: 95145
Taken BR backward: 128670
Not taken BR: 325663
Not taken BR forward: 212136
Not taken BR backward: 113527
Mispredicted instructions: 355759
Mispredicted BR: 223815
Mispredicted BR taken: 223815
Mispredicted BR forward taken: 95145
Mispredicted BR backward taken: 128670
Mispredicted BR not taken: 0
Mispredicted BR forward not taken: 0
Mispredicted BR backward not taken: 0
Mispredicted JALR: 38056
Mispredicted CALL: 38054
Mispredicted RET: 38055
Partial instructions: 0
Instruction buffer full: 0
Instruction buffer dead: 8456
Wait source dependency: 968294
Wait MUL unit: 0
Wait DIV unit: 61694
Wait data request: 44700
Wait data acknowledgement: 83724
Empty buffer for misaligned instructions: 0
Empty fetch port: 718951
Empty commit port: 2339145
L1I hits: 0
L1I misses: 0
L1I prefetches: 0
L1D hits: 0
L1D misses: 0
L1D prefetches: 0
L2 hits: 0
L2 misses: 0
L2 prefetches: 0
------------------------------

EXEC NAME: slre
[1;32mTEST REPORT: SUCCESS.[0m
Real cycles: 4404569
Real instructions: 2590543
BOOT file: /home/mrabiai/Bureau/herd-ware/sw/embench-iot/hex/SIM/WAESP32AU1V010F/slre.boot8.hex
iROM file: /home/mrabiai/Bureau/herd-ware/sw/embench-iot/hex/SIM/WAESP32AU1V010F/slre.irom8.hex
Simulation fast clock cycles (/1): 8890100
Simulation main clock cycles (/2): 4445050

------------------------------
           HART: 0
------------------------------
Cycles: 4445045
Time: 4445045
Retired instructions: 2614382
ALU instructions: 1826109
BRU instructions: 665499
MUL instructions: 0
DIV instructions: 0
Load instructions: 590566
Store instructions: 297430
BR instructions: 534601
BR forward instructions: 440463
BR backward instructions: 94138
JAL instructions: 98028
JALR instructions: 32870
CALL instructions: 32868
RET instructions: 32869
Read cycle instructions: 2
Cache flush instructions: 0
16-bit instructions: 0
32-bit instructions: 2614382
0 read port: 119800
1 read port: 1406216
2 read port: 1088366
Taken BR: 180270
Taken BR forward: 131980
Taken BR backward: 48290
Not taken BR: 354331
Not taken BR forward: 308483
Not taken BR backward: 45848
Mispredicted instructions: 312944
Mispredicted BR: 182046
Mispredicted BR taken: 180270
Mispredicted BR forward taken: 131980
Mispredicted BR backward taken: 48290
Mispredicted BR not taken: 1776
Mispredicted BR forward not taken: 1776
Mispredicted BR backward not taken: 0
Mispredicted JALR: 32870
Mispredicted CALL: 32868
Mispredicted RET: 32869
Partial instructions: 0
Instruction buffer full: 0
Instruction buffer dead: 32745
Wait source dependency: 671458
Wait MUL unit: 0
Wait DIV unit: 0
Wait data request: 13098
Wait data acknowledgement: 236656
Empty buffer for misaligned instructions: 0
Empty fetch port: 658634
Empty commit port: 1830663
L1I hits: 0
L1I misses: 0
L1I prefetches: 0
L1D hits: 0
L1D misses: 0
L1D prefetches: 0
L2 hits: 0
L2 misses: 0
L2 prefetches: 0
------------------------------

EXEC NAME: st
[1;31mTEST REPORT: FAILED.[0m
Real cycles: 6303802
Real instructions: 3936305
BOOT file: /home/mrabiai/Bureau/herd-ware/sw/embench-iot/hex/SIM/WAESP32AU1V010F/st.boot8.hex
iROM file: /home/mrabiai/Bureau/herd-ware/sw/embench-iot/hex/SIM/WAESP32AU1V010F/st.irom8.hex
Simulation fast clock cycles (/1): 13581618
Simulation main clock cycles (/2): 6790809

------------------------------
           HART: 0
------------------------------
Cycles: 6790804
Time: 6790804
Retired instructions: 4240434
ALU instructions: 3473462
BRU instructions: 584347
MUL instructions: 146664
DIV instructions: 25760
Load instructions: 242441
Store instructions: 204052
BR instructions: 445249
BR forward instructions: 416840
BR backward instructions: 28409
JAL instructions: 94911
JALR instructions: 44187
CALL instructions: 44185
RET instructions: 44186
Read cycle instructions: 2
Cache flush instructions: 0
16-bit instructions: 0
32-bit instructions: 4240434
0 read port: 230486
1 read port: 2089628
2 read port: 1920320
Taken BR: 192202
Taken BR forward: 178754
Taken BR backward: 13448
Not taken BR: 253047
Not taken BR forward: 238086
Not taken BR backward: 14961
Mispredicted instructions: 331300
Mispredicted BR: 192202
Mispredicted BR taken: 192202
Mispredicted BR forward taken: 178754
Mispredicted BR backward taken: 13448
Mispredicted BR not taken: 0
Mispredicted BR forward not taken: 0
Mispredicted BR backward not taken: 0
Mispredicted JALR: 44187
Mispredicted CALL: 44185
Mispredicted RET: 44186
Partial instructions: 0
Instruction buffer full: 0
Instruction buffer dead: 35953
Wait source dependency: 149758
Wait MUL unit: 371448
Wait DIV unit: 749112
Wait data request: 14
Wait data acknowledgement: 71369
Empty buffer for misaligned instructions: 0
Empty fetch port: 695684
Empty commit port: 2550370
L1I hits: 0
L1I misses: 0
L1I prefetches: 0
L1D hits: 0
L1D misses: 0
L1D prefetches: 0
L2 hits: 0
L2 misses: 0
L2 prefetches: 0
------------------------------

EXEC NAME: statemate
[1;32mTEST REPORT: SUCCESS.[0m
Real cycles: 1850135
Real instructions: 1278596
BOOT file: /home/mrabiai/Bureau/herd-ware/sw/embench-iot/hex/SIM/WAESP32AU1V010F/statemate.boot8.hex
iROM file: /home/mrabiai/Bureau/herd-ware/sw/embench-iot/hex/SIM/WAESP32AU1V010F/statemate.irom8.hex
Simulation fast clock cycles (/1): 3704662
Simulation main clock cycles (/2): 1852331

------------------------------
           HART: 0
------------------------------
Cycles: 1852326
Time: 1852326
Retired instructions: 1280044
ALU instructions: 894562
BRU instructions: 141670
MUL instructions: 0
DIV instructions: 0
Load instructions: 471841
Store instructions: 528693
BR instructions: 106270
BR forward instructions: 86532
BR backward instructions: 19738
JAL instructions: 19667
JALR instructions: 15733
CALL instructions: 15732
RET instructions: 15733
Read cycle instructions: 2
Cache flush instructions: 0
16-bit instructions: 0
32-bit instructions: 1280044
0 read port: 31472
1 read port: 611605
2 read port: 636967
Taken BR: 68854
Taken BR forward: 51092
Taken BR backward: 17762
Not taken BR: 37416
Not taken BR forward: 35440
Not taken BR backward: 1976
Mispredicted instructions: 104254
Mispredicted BR: 68854
Mispredicted BR taken: 68854
Mispredicted BR forward taken: 51092
Mispredicted BR backward taken: 17762
Mispredicted BR not taken: 0
Mispredicted BR forward not taken: 0
Mispredicted BR backward not taken: 0
Mispredicted JALR: 15733
Mispredicted CALL: 15732
Mispredicted RET: 15733
Partial instructions: 0
Instruction buffer full: 0
Instruction buffer dead: 0
Wait source dependency: 151405
Wait MUL unit: 0
Wait DIV unit: 0
Wait data request: 141482
Wait data acknowledgement: 53059
Empty buffer for misaligned instructions: 0
Empty fetch port: 208509
Empty commit port: 572282
L1I hits: 0
L1I misses: 0
L1I prefetches: 0
L1D hits: 0
L1D misses: 0
L1D prefetches: 0
L2 hits: 0
L2 misses: 0
L2 prefetches: 0
------------------------------

EXEC NAME: tarfind
[1;32mTEST REPORT: SUCCESS.[0m
Real cycles: 2448877
Real instructions: 1037258
BOOT file: /home/mrabiai/Bureau/herd-ware/sw/embench-iot/hex/SIM/WAESP32AU1V010F/tarfind.boot8.hex
iROM file: /home/mrabiai/Bureau/herd-ware/sw/embench-iot/hex/SIM/WAESP32AU1V010F/tarfind.irom8.hex
Simulation fast clock cycles (/1): 5016930
Simulation main clock cycles (/2): 2508465

------------------------------
           HART: 0
------------------------------
Cycles: 2508460
Time: 2508460
Retired instructions: 1064152
ALU instructions: 774920
BRU instructions: 193832
MUL instructions: 36960
DIV instructions: 36960
Load instructions: 80614
Store instructions: 206835
BR instructions: 109995
BR forward instructions: 28111
BR backward instructions: 81884
JAL instructions: 40383
JALR instructions: 43454
CALL instructions: 40332
RET instructions: 40333
Read cycle instructions: 2
Cache flush instructions: 0
16-bit instructions: 0
32-bit instructions: 1064152
0 read port: 154748
1 read port: 471678
2 read port: 437726
Taken BR: 89418
Taken BR forward: 12770
Taken BR backward: 76648
Not taken BR: 20577
Not taken BR forward: 15341
Not taken BR backward: 5236
Mispredicted instructions: 173159
Mispredicted BR: 89418
Mispredicted BR taken: 89418
Mispredicted BR forward taken: 12770
Mispredicted BR backward taken: 76648
Mispredicted BR not taken: 0
Mispredicted BR forward not taken: 0
Mispredicted BR backward not taken: 0
Mispredicted JALR: 43358
Mispredicted CALL: 40332
Mispredicted RET: 40333
Partial instructions: 0
Instruction buffer full: 0
Instruction buffer dead: 36914
Wait source dependency: 71033
Wait MUL unit: 110878
Wait DIV unit: 554273
Wait data request: 0
Wait data acknowledgement: 4
Empty buffer for misaligned instructions: 0
Empty fetch port: 383276
Empty commit port: 1444308
L1I hits: 0
L1I misses: 0
L1I prefetches: 0
L1D hits: 0
L1D misses: 0
L1D prefetches: 0
L2 hits: 0
L2 misses: 0
L2 prefetches: 0
------------------------------

EXEC NAME: ud
[1;31mTEST REPORT: FAILED.[0m
Real cycles: 6012574
Real instructions: 3358071
BOOT file: /home/mrabiai/Bureau/herd-ware/sw/embench-iot/hex/SIM/WAESP32AU1V010F/ud.boot8.hex
iROM file: /home/mrabiai/Bureau/herd-ware/sw/embench-iot/hex/SIM/WAESP32AU1V010F/ud.irom8.hex
Simulation fast clock cycles (/1): 12036406
Simulation main clock cycles (/2): 6018203

------------------------------
           HART: 0
------------------------------
Cycles: 6018198
Time: 6018198
Retired instructions: 3361308
ALU instructions: 2595014
BRU instructions: 597678
MUL instructions: 128673
DIV instructions: 31059
Load instructions: 448203
Store instructions: 210536
BR instructions: 480804
BR forward instructions: 201154
BR backward instructions: 279650
JAL instructions: 79885
JALR instructions: 36989
CALL instructions: 36988
RET instructions: 36989
Read cycle instructions: 2
Cache flush instructions: 0
16-bit instructions: 0
32-bit instructions: 3361308
0 read port: 130189
1 read port: 1822431
2 read port: 1408688
Taken BR: 281124
Taken BR forward: 97615
Taken BR backward: 183509
Not taken BR: 199680
Not taken BR forward: 103539
Not taken BR backward: 96141
Mispredicted instructions: 400956
Mispredicted BR: 284082
Mispredicted BR taken: 281124
Mispredicted BR forward taken: 97615
Mispredicted BR backward taken: 183509
Mispredicted BR not taken: 2958
Mispredicted BR forward not taken: 0
Mispredicted BR backward not taken: 2958
Mispredicted JALR: 36989
Mispredicted CALL: 36988
Mispredicted RET: 36989
Partial instructions: 0
Instruction buffer full: 0
Instruction buffer dead: 25143
Wait source dependency: 772054
Wait MUL unit: 291363
Wait DIV unit: 492507
Wait data request: 0
Wait data acknowledgement: 63601
Empty buffer for misaligned instructions: 0
Empty fetch port: 827056
Empty commit port: 2656890
L1I hits: 0
L1I misses: 0
L1I prefetches: 0
L1D hits: 0
L1D misses: 0
L1D prefetches: 0
L2 hits: 0
L2 misses: 0
L2 prefetches: 0
------------------------------

EXEC NAME: wikisort
[1;31mTEST REPORT: FAILED.[0m
Real cycles: 2296530
Real instructions: 1266807
BOOT file: /home/mrabiai/Bureau/herd-ware/sw/embench-iot/hex/SIM/WAESP32AU1V010F/wikisort.boot8.hex
iROM file: /home/mrabiai/Bureau/herd-ware/sw/embench-iot/hex/SIM/WAESP32AU1V010F/wikisort.irom8.hex
Simulation fast clock cycles (/1): 9197826
Simulation main clock cycles (/2): 4598913

------------------------------
           HART: 0
------------------------------
Cycles: 4598908
Time: 4598908
Retired instructions: 2537592
ALU instructions: 2031247
BRU instructions: 424425
MUL instructions: 58400
DIV instructions: 19308
Load instructions: 390176
Store instructions: 224616
BR instructions: 267063
BR forward instructions: 195108
BR backward instructions: 71955
JAL instructions: 41261
JALR instructions: 116101
CALL instructions: 69151
RET instructions: 69152
Read cycle instructions: 2
Cache flush instructions: 0
16-bit instructions: 0
32-bit instructions: 2537592
0 read port: 97565
1 read port: 1473263
2 read port: 966764
Taken BR: 143274
Taken BR forward: 83605
Taken BR backward: 59669
Not taken BR: 123789
Not taken BR forward: 111503
Not taken BR backward: 12286
Mispredicted instructions: 300636
Mispredicted BR: 143274
Mispredicted BR taken: 143274
Mispredicted BR forward taken: 83605
Mispredicted BR backward taken: 59669
Mispredicted BR not taken: 0
Mispredicted BR forward not taken: 0
Mispredicted BR backward not taken: 0
Mispredicted JALR: 116101
Mispredicted CALL: 69151
Mispredicted RET: 69152
Partial instructions: 0
Instruction buffer full: 0
Instruction buffer dead: 23492
Wait source dependency: 212200
Wait MUL unit: 97948
Wait DIV unit: 551264
Wait data request: 72
Wait data acknowledgement: 47632
Empty buffer for misaligned instructions: 0
Empty fetch port: 622383
Empty commit port: 2061316
L1I hits: 0
L1I misses: 0
L1I prefetches: 0
L1D hits: 0
L1D misses: 0
L1D prefetches: 0
L2 hits: 0
L2 misses: 0
L2 prefetches: 0
------------------------------



"""

extract_cpi(report_data)
