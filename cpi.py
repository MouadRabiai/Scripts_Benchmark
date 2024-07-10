import re

def extract_cpi(report):

    exec_blocks = re.findall(r"EXEC NAME: (.+?)\n.*?Real cycles: (\d+).*?Real instructions: (\d+)", report, re.DOTALL)

    for exec_name, cycles, instructions in exec_blocks:

        cycles = int(cycles)
        instructions = int(instructions)


        cpi = cycles / instructions if instructions != 0 else float('inf')


        print(f"{exec_name}: CPI = {cpi:.3f}")


report_data = """
EXEC NAME: aha-mont64
[1;32mTEST REPORT: SUCCESS.[0m
Real cycles: 4986855
Real instructions: 4531262
BOOT file: /home/mrabiai/Bureau/herd-ware/sw/embench-iot/hex/SIM/WAESP32AU1V010/aha-mont64.boot8.hex
iROM file: /home/mrabiai/Bureau/herd-ware/sw/embench-iot/hex/SIM/WAESP32AU1V010/aha-mont64.irom8.hex
Simulation fast clock cycles (/1): 9998268
Simulation main clock cycles (/2): 4999134

------------------------------
           HART: 0
------------------------------
Cycles: 4999129
Time: 4999129
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
Mispredicted instructions: 104780
Mispredicted BR: 101787
Mispredicted BR taken: 63627
Mispredicted BR forward taken: 53020
Mispredicted BR backward taken: 10607
Mispredicted BR not taken: 38160
Mispredicted BR forward not taken: 30528
Mispredicted BR backward not taken: 7632
Mispredicted JALR: 434
Mispredicted CALL: 1284
Mispredicted RET: 434
Partial instructions: 0
Instruction buffer full: 0
Instruction buffer dead: 0
Wait source dependency: 2136
Wait MUL unit: 35632
Wait DIV unit: 0
Wait data request: 430
Wait data acknowledgement: 438
Empty buffer for misaligned instructions: 0
Empty fetch port: 209562
Empty commit port: 456459
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
[1;32mTEST REPORT: SUCCESS.[0m
Real cycles: 4355467
Real instructions: 3831161
BOOT file: /home/mrabiai/Bureau/herd-ware/sw/embench-iot/hex/SIM/WAESP32AU1V010/crc32.boot8.hex
iROM file: /home/mrabiai/Bureau/herd-ware/sw/embench-iot/hex/SIM/WAESP32AU1V010/crc32.irom8.hex
Simulation fast clock cycles (/1): 8762858
Simulation main clock cycles (/2): 4381429

------------------------------
           HART: 0
------------------------------
Cycles: 4381424
Time: 4381424
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
Mispredicted instructions: 549
Mispredicted BR: 348
Mispredicted BR taken: 176
Mispredicted BR forward taken: 1
Mispredicted BR backward taken: 175
Mispredicted BR not taken: 172
Mispredicted BR forward not taken: 0
Mispredicted BR backward not taken: 172
Mispredicted JALR: 184
Mispredicted CALL: 14
Mispredicted RET: 184
Partial instructions: 0
Instruction buffer full: 0
Instruction buffer dead: 0
Wait source dependency: 350219
Wait MUL unit: 175104
Wait DIV unit: 0
Wait data request: 0
Wait data acknowledgement: 4
Empty buffer for misaligned instructions: 0
Empty fetch port: 1100
Empty commit port: 527522
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
[1;32mTEST REPORT: SUCCESS.[0m
Real cycles: 9936030
Real instructions: 7074897
BOOT file: /home/mrabiai/Bureau/herd-ware/sw/embench-iot/hex/SIM/WAESP32AU1V010/cubic.boot8.hex
iROM file: /home/mrabiai/Bureau/herd-ware/sw/embench-iot/hex/SIM/WAESP32AU1V010/cubic.irom8.hex
Simulation fast clock cycles (/1): 21862578
Simulation main clock cycles (/2): 10931289

------------------------------
           HART: 0
------------------------------
Cycles: 10931284
Time: 10931284
Retired instructions: 7783530
ALU instructions: 6402860
BRU instructions: 975663
MUL instructions: 372746
DIV instructions: 27368
Load instructions: 663026
Store instructions: 616494
BR instructions: 815722
BR forward instructions: 642267
BR backward instructions: 173455
JAL instructions: 112134
JALR instructions: 47807
CALL instructions: 47563
RET instructions: 47564
Read cycle instructions: 2
Cache flush instructions: 0
16-bit instructions: 0
32-bit instructions: 7783530
0 read port: 331814
1 read port: 3541032
2 read port: 3910684
Taken BR: 421917
Taken BR forward: 311327
Taken BR backward: 110590
Not taken BR: 393805
Not taken BR forward: 330940
Not taken BR backward: 62865
Mispredicted instructions: 461351
Mispredicted BR: 318843
Mispredicted BR taken: 281388
Mispredicted BR forward taken: 238689
Mispredicted BR backward taken: 42699
Mispredicted BR not taken: 37455
Mispredicted BR forward not taken: 10536
Mispredicted BR backward not taken: 26919
Mispredicted JALR: 40828
Mispredicted CALL: 47068
Mispredicted RET: 40585
Partial instructions: 0
Instruction buffer full: 0
Instruction buffer dead: 23618
Wait source dependency: 397559
Wait MUL unit: 372746
Wait DIV unit: 559680
Wait data request: 45837
Wait data acknowledgement: 106581
Empty buffer for misaligned instructions: 0
Empty fetch port: 941514
Empty commit port: 3075368
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
[1;32mTEST REPORT: SUCCESS.[0m
Real cycles: 4538472
Real instructions: 3499382
BOOT file: /home/mrabiai/Bureau/herd-ware/sw/embench-iot/hex/SIM/WAESP32AU1V010/edn.boot8.hex
iROM file: /home/mrabiai/Bureau/herd-ware/sw/embench-iot/hex/SIM/WAESP32AU1V010/edn.irom8.hex
Simulation fast clock cycles (/1): 9188642
Simulation main clock cycles (/2): 4594321

------------------------------
           HART: 0
------------------------------
Cycles: 4594316
Time: 4594316
Retired instructions: 3542416
ALU instructions: 1759545
BRU instructions: 360606
MUL instructions: 580008
DIV instructions: 0
Load instructions: 906601
Store instructions: 111105
BR instructions: 359782
BR forward instructions: 389
BR backward instructions: 359393
JAL instructions: 458
JALR instructions: 366
CALL instructions: 365
RET instructions: 366
Read cycle instructions: 2
Cache flush instructions: 0
16-bit instructions: 0
32-bit instructions: 3542416
0 read port: 571
1 read port: 1822207
2 read port: 1719638
Taken BR: 348304
Taken BR forward: 92
Taken BR backward: 348212
Not taken BR: 11478
Not taken BR forward: 297
Not taken BR backward: 11181
Mispredicted instructions: 22513
Mispredicted BR: 22468
Mispredicted BR taken: 11289
Mispredicted BR forward taken: 92
Mispredicted BR backward taken: 11197
Mispredicted BR not taken: 11179
Mispredicted BR forward not taken: 0
Mispredicted BR backward not taken: 11179
Mispredicted JALR: 20
Mispredicted CALL: 19
Mispredicted RET: 20
Partial instructions: 0
Instruction buffer full: 0
Instruction buffer dead: 0
Wait source dependency: 609053
Wait MUL unit: 580008
Wait DIV unit: 0
Wait data request: 7392
Wait data acknowledgement: 8982
Empty buffer for misaligned instructions: 0
Empty fetch port: 45027
Empty commit port: 1051366
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
Real cycles: 3381560
Real instructions: 2450506
BOOT file: /home/mrabiai/Bureau/herd-ware/sw/embench-iot/hex/SIM/WAESP32AU1V010/huffbench.boot8.hex
iROM file: /home/mrabiai/Bureau/herd-ware/sw/embench-iot/hex/SIM/WAESP32AU1V010/huffbench.irom8.hex
Simulation fast clock cycles (/1): 7392350
Simulation main clock cycles (/2): 3696175

------------------------------
           HART: 0
------------------------------
Cycles: 3696170
Time: 3696170
Retired instructions: 2678866
ALU instructions: 1919444
BRU instructions: 598002
MUL instructions: 0
DIV instructions: 0
Load instructions: 504579
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
32-bit instructions: 2678866
0 read port: 54331
1 read port: 1631118
2 read port: 993417
Taken BR: 310595
Taken BR forward: 60364
Taken BR backward: 250231
Not taken BR: 234683
Not taken BR forward: 209707
Not taken BR backward: 24976
Mispredicted instructions: 103092
Mispredicted BR: 102664
Mispredicted BR taken: 66813
Mispredicted BR forward taken: 46630
Mispredicted BR backward taken: 20183
Mispredicted BR not taken: 35851
Mispredicted BR forward not taken: 16411
Mispredicted BR backward not taken: 19440
Mispredicted JALR: 123
Mispredicted CALL: 169
Mispredicted RET: 110
Partial instructions: 0
Instruction buffer full: 0
Instruction buffer dead: 125
Wait source dependency: 597732
Wait MUL unit: 0
Wait DIV unit: 0
Wait data request: 384
Wait data acknowledgement: 1263
Empty buffer for misaligned instructions: 0
Empty fetch port: 206310
Empty commit port: 1016041
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
Real cycles: 4074814
Real instructions: 3183124
BOOT file: /home/mrabiai/Bureau/herd-ware/sw/embench-iot/hex/SIM/WAESP32AU1V010/matmult-int.boot8.hex
iROM file: /home/mrabiai/Bureau/herd-ware/sw/embench-iot/hex/SIM/WAESP32AU1V010/matmult-int.irom8.hex
Simulation fast clock cycles (/1): 8392730
Simulation main clock cycles (/2): 4196365

------------------------------
           HART: 0
------------------------------
Cycles: 4196360
Time: 4196360
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
Mispredicted instructions: 39899
Mispredicted BR: 39869
Mispredicted BR taken: 19943
Mispredicted BR forward taken: 3
Mispredicted BR backward taken: 19940
Mispredicted BR not taken: 19926
Mispredicted BR forward not taken: 0
Mispredicted BR backward not taken: 19926
Mispredicted JALR: 12
Mispredicted CALL: 14
Mispredicted RET: 12
Partial instructions: 0
Instruction buffer full: 0
Instruction buffer dead: 800
Wait source dependency: 753212
Wait MUL unit: 376000
Wait DIV unit: 15945
Wait data request: 0
Wait data acknowledgement: 4
Empty buffer for misaligned instructions: 0
Empty fetch port: 80600
Empty commit port: 929556
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
Real cycles: 2139873
Real instructions: 2046782
BOOT file: /home/mrabiai/Bureau/herd-ware/sw/embench-iot/hex/SIM/WAESP32AU1V010/md5sum.boot8.hex
iROM file: /home/mrabiai/Bureau/herd-ware/sw/embench-iot/hex/SIM/WAESP32AU1V010/md5sum.irom8.hex
Simulation fast clock cycles (/1): 4369210
Simulation main clock cycles (/2): 2184605

------------------------------
           HART: 0
------------------------------
Cycles: 2184600
Time: 2184600
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
Mispredicted instructions: 10209
Mispredicted BR: 9176
Mispredicted BR taken: 6393
Mispredicted BR forward taken: 4306
Mispredicted BR backward taken: 2087
Mispredicted BR not taken: 2783
Mispredicted BR forward not taken: 1624
Mispredicted BR backward not taken: 1159
Mispredicted JALR: 444
Mispredicted CALL: 415
Mispredicted RET: 391
Partial instructions: 0
Instruction buffer full: 0
Instruction buffer dead: 0
Wait source dependency: 54089
Wait MUL unit: 52
Wait DIV unit: 0
Wait data request: 104
Wait data acknowledgement: 160
Empty buffer for misaligned instructions: 0
Empty fetch port: 20419
Empty commit port: 94924
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
[1;32mTEST REPORT: SUCCESS.[0m
Real cycles: 7556980
Real instructions: 4927371
BOOT file: /home/mrabiai/Bureau/herd-ware/sw/embench-iot/hex/SIM/WAESP32AU1V010/minver.boot8.hex
iROM file: /home/mrabiai/Bureau/herd-ware/sw/embench-iot/hex/SIM/WAESP32AU1V010/minver.irom8.hex
Simulation fast clock cycles (/1): 15147828
Simulation main clock cycles (/2): 7573914

------------------------------
           HART: 0
------------------------------
Cycles: 7573909
Time: 7573909
Retired instructions: 4939000
ALU instructions: 3907581
BRU instructions: 920210
MUL instructions: 73392
DIV instructions: 35584
Load instructions: 420583
Store instructions: 385548
BR instructions: 713748
BR forward instructions: 630268
BR backward instructions: 83480
JAL instructions: 138557
JALR instructions: 67905
CALL instructions: 67348
RET instructions: 67349
Read cycle instructions: 2
Cache flush instructions: 0
16-bit instructions: 0
32-bit instructions: 4939000
0 read port: 297666
1 read port: 2733273
2 read port: 1908061
Taken BR: 332220
Taken BR forward: 289355
Taken BR backward: 42865
Not taken BR: 381528
Not taken BR forward: 340913
Not taken BR backward: 40615
Mispredicted instructions: 388225
Mispredicted BR: 240822
Mispredicted BR taken: 223032
Mispredicted BR forward taken: 187425
Mispredicted BR backward taken: 35607
Mispredicted BR not taken: 17790
Mispredicted BR forward not taken: 11115
Mispredicted BR backward not taken: 6675
Mispredicted JALR: 32267
Mispredicted CALL: 55639
Mispredicted RET: 31711
Partial instructions: 0
Instruction buffer full: 0
Instruction buffer dead: 32805
Wait source dependency: 139598
Wait MUL unit: 73392
Wait DIV unit: 879592
Wait data request: 1668
Wait data acknowledgement: 27259
Empty buffer for misaligned instructions: 0
Empty fetch port: 803144
Empty commit port: 2623225
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
[1;32mTEST REPORT: SUCCESS.[0m
Real cycles: 4677592
Real instructions: 3473819
BOOT file: /home/mrabiai/Bureau/herd-ware/sw/embench-iot/hex/SIM/WAESP32AU1V010/nbody.boot8.hex
iROM file: /home/mrabiai/Bureau/herd-ware/sw/embench-iot/hex/SIM/WAESP32AU1V010/nbody.irom8.hex
Simulation fast clock cycles (/1): 18717310
Simulation main clock cycles (/2): 9358655

------------------------------
           HART: 0
------------------------------
Cycles: 9358650
Time: 9358650
Retired instructions: 6951583
ALU instructions: 5591759
BRU instructions: 1107242
MUL instructions: 232756
DIV instructions: 16216
Load instructions: 343985
Store instructions: 277435
BR instructions: 938673
BR forward instructions: 712883
BR backward instructions: 225790
JAL instructions: 118386
JALR instructions: 50183
CALL instructions: 50178
RET instructions: 50179
Read cycle instructions: 2
Cache flush instructions: 0
16-bit instructions: 0
32-bit instructions: 6951583
0 read port: 291512
1 read port: 3383356
2 read port: 3276715
Taken BR: 450164
Taken BR forward: 300844
Taken BR backward: 149320
Not taken BR: 488509
Not taken BR forward: 412039
Not taken BR backward: 76470
Mispredicted instructions: 413093
Mispredicted BR: 268126
Mispredicted BR taken: 237520
Mispredicted BR forward taken: 202669
Mispredicted BR backward taken: 34851
Mispredicted BR not taken: 30606
Mispredicted BR forward not taken: 16197
Mispredicted BR backward not taken: 14409
Mispredicted JALR: 38512
Mispredicted CALL: 45913
Mispredicted RET: 38508
Partial instructions: 0
Instruction buffer full: 0
Instruction buffer dead: 19821
Wait source dependency: 67168
Wait MUL unit: 232756
Wait DIV unit: 476778
Wait data request: 0
Wait data acknowledgement: 25239
Empty buffer for misaligned instructions: 0
Empty fetch port: 843981
Empty commit port: 2407042
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
Real cycles: 4562423
Real instructions: 4406508
BOOT file: /home/mrabiai/Bureau/herd-ware/sw/embench-iot/hex/SIM/WAESP32AU1V010/nettle-aes.boot8.hex
iROM file: /home/mrabiai/Bureau/herd-ware/sw/embench-iot/hex/SIM/WAESP32AU1V010/nettle-aes.irom8.hex
Simulation fast clock cycles (/1): 9254000
Simulation main clock cycles (/2): 4627000

------------------------------
           HART: 0
------------------------------
Cycles: 4626995
Time: 4626995
Retired instructions: 4468616
ALU instructions: 4285160
BRU instructions: 78934
MUL instructions: 0
DIV instructions: 8216
Load instructions: 819402
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
32-bit instructions: 4468616
0 read port: 2087
1 read port: 3054678
2 read port: 1411851
Taken BR: 48867
Taken BR forward: 239
Taken BR backward: 48628
Not taken BR: 29011
Not taken BR forward: 10283
Not taken BR backward: 18728
Mispredicted instructions: 14919
Mispredicted BR: 14173
Mispredicted BR taken: 5874
Mispredicted BR forward taken: 239
Mispredicted BR backward taken: 5635
Mispredicted BR not taken: 8299
Mispredicted BR forward not taken: 0
Mispredicted BR backward not taken: 8299
Mispredicted JALR: 254
Mispredicted CALL: 407
Mispredicted RET: 253
Partial instructions: 0
Instruction buffer full: 0
Instruction buffer dead: 4424
Wait source dependency: 69154
Wait MUL unit: 0
Wait DIV unit: 52456
Wait data request: 9480
Wait data acknowledgement: 8378
Empty buffer for misaligned instructions: 0
Empty fetch port: 38055
Empty commit port: 155847
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
Real cycles: 4186460
Real instructions: 3992435
BOOT file: /home/mrabiai/Bureau/herd-ware/sw/embench-iot/hex/SIM/WAESP32AU1V010/nettle-sha256.boot8.hex
iROM file: /home/mrabiai/Bureau/herd-ware/sw/embench-iot/hex/SIM/WAESP32AU1V010/nettle-sha256.irom8.hex
Simulation fast clock cycles (/1): 8392342
Simulation main clock cycles (/2): 4196171

------------------------------
           HART: 0
------------------------------
Cycles: 4196166
Time: 4196166
Retired instructions: 4001546
ALU instructions: 3884810
BRU instructions: 48168
MUL instructions: 0
DIV instructions: 0
Load instructions: 399530
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
32-bit instructions: 4001546
0 read port: 8122
1 read port: 1767753
2 read port: 2225671
Taken BR: 27175
Taken BR forward: 3333
Taken BR backward: 23842
Not taken BR: 11444
Not taken BR forward: 5250
Not taken BR backward: 6194
Mispredicted instructions: 19850
Mispredicted BR: 10969
Mispredicted BR taken: 7632
Mispredicted BR forward taken: 3333
Mispredicted BR backward taken: 4299
Mispredicted BR not taken: 3337
Mispredicted BR forward not taken: 0
Mispredicted BR backward not taken: 3337
Mispredicted JALR: 3154
Mispredicted CALL: 3344
Mispredicted RET: 2677
Partial instructions: 0
Instruction buffer full: 0
Instruction buffer dead: 0
Wait source dependency: 98081
Wait MUL unit: 0
Wait DIV unit: 0
Wait data request: 6664
Wait data acknowledgement: 25708
Empty buffer for misaligned instructions: 0
Empty fetch port: 39701
Empty commit port: 172720
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
BOOT file: /home/mrabiai/Bureau/herd-ware/sw/embench-iot/hex/SIM/WAESP32AU1V010/nsichneu.boot8.hex
iROM file: /home/mrabiai/Bureau/herd-ware/sw/embench-iot/hex/SIM/WAESP32AU1V010/nsichneu.irom8.hex
Simulation fast clock cycles (/1): 12474002
Simulation main clock cycles (/2): 6237001

------------------------------
           HART: 0
------------------------------
Cycles: 6236996
Time: 6236996
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
Mispredicted instructions: 422615
Mispredicted BR: 186042
Mispredicted BR taken: 186039
Mispredicted BR forward taken: 147843
Mispredicted BR backward taken: 38196
Mispredicted BR not taken: 3
Mispredicted BR forward not taken: 0
Mispredicted BR backward not taken: 3
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
Empty fetch port: 845231
Empty commit port: 3996812
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
[1;32mTEST REPORT: SUCCESS.[0m
Real cycles: 4586493
Real instructions: 3787005
BOOT file: /home/mrabiai/Bureau/herd-ware/sw/embench-iot/hex/SIM/WAESP32AU1V010/picojpeg.boot8.hex
iROM file: /home/mrabiai/Bureau/herd-ware/sw/embench-iot/hex/SIM/WAESP32AU1V010/picojpeg.irom8.hex
Simulation fast clock cycles (/1): 10706434
Simulation main clock cycles (/2): 5353217

------------------------------
           HART: 0
------------------------------
Cycles: 5353212
Time: 5353212
Retired instructions: 4419658
ALU instructions: 3321319
BRU instructions: 478978
MUL instructions: 123116
DIV instructions: 0
Load instructions: 644344
Store instructions: 581925
BR instructions: 401542
BR forward instructions: 218789
BR backward instructions: 182753
JAL instructions: 51772
JALR instructions: 25664
CALL instructions: 24466
RET instructions: 24467
Read cycle instructions: 2
Cache flush instructions: 0
16-bit instructions: 0
32-bit instructions: 4419658
0 read port: 65915
1 read port: 2645982
2 read port: 1707761
Taken BR: 318375
Taken BR forward: 154581
Taken BR backward: 163794
Not taken BR: 83167
Not taken BR forward: 64208
Not taken BR backward: 18959
Mispredicted instructions: 64868
Mispredicted BR: 39577
Mispredicted BR taken: 31397
Mispredicted BR forward taken: 24376
Mispredicted BR backward taken: 7021
Mispredicted BR not taken: 8180
Mispredicted BR forward not taken: 5163
Mispredicted BR backward not taken: 3017
Mispredicted JALR: 8960
Mispredicted CALL: 6093
Mispredicted RET: 7763
Partial instructions: 0
Instruction buffer full: 0
Instruction buffer dead: 5501
Wait source dependency: 389861
Wait MUL unit: 123116
Wait DIV unit: 0
Wait data request: 104895
Wait data acknowledgement: 76822
Empty buffer for misaligned instructions: 0
Empty fetch port: 135273
Empty commit port: 911283
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
Real cycles: 3763749
Real instructions: 2148524
BOOT file: /home/mrabiai/Bureau/herd-ware/sw/embench-iot/hex/SIM/WAESP32AU1V010/primecount.boot8.hex
iROM file: /home/mrabiai/Bureau/herd-ware/sw/embench-iot/hex/SIM/WAESP32AU1V010/primecount.irom8.hex
Simulation fast clock cycles (/1): 15055538
Simulation main clock cycles (/2): 7527769

------------------------------
           HART: 0
------------------------------
Cycles: 7527764
Time: 7527764
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
Mispredicted instructions: 211357
Mispredicted BR: 211329
Mispredicted BR taken: 132848
Mispredicted BR forward taken: 132834
Mispredicted BR backward taken: 14
Mispredicted BR not taken: 78481
Mispredicted BR forward not taken: 78479
Mispredicted BR backward not taken: 2
Mispredicted JALR: 11
Mispredicted CALL: 13
Mispredicted RET: 11
Partial instructions: 0
Instruction buffer full: 0
Instruction buffer dead: 0
Wait source dependency: 2319503
Wait MUL unit: 131516
Wait DIV unit: 0
Wait data request: 0
Wait data acknowledgement: 4
Empty buffer for misaligned instructions: 0
Empty fetch port: 422716
Empty commit port: 3230552
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
[1;32mTEST REPORT: SUCCESS.[0m
Real cycles: 3928919
Real instructions: 2793650
BOOT file: /home/mrabiai/Bureau/herd-ware/sw/embench-iot/hex/SIM/WAESP32AU1V010/qrduino.boot8.hex
iROM file: /home/mrabiai/Bureau/herd-ware/sw/embench-iot/hex/SIM/WAESP32AU1V010/qrduino.irom8.hex
Simulation fast clock cycles (/1): 9439332
Simulation main clock cycles (/2): 4719666

------------------------------
           HART: 0
------------------------------
Cycles: 4719661
Time: 4719661
Retired instructions: 3356987
ALU instructions: 2318660
BRU instructions: 501206
MUL instructions: 94158
DIV instructions: 0
Load instructions: 604644
Store instructions: 83386
BR instructions: 470937
BR forward instructions: 218120
BR backward instructions: 252817
JAL instructions: 27523
JALR instructions: 2746
CALL instructions: 2666
RET instructions: 2667
Read cycle instructions: 2
Cache flush instructions: 0
16-bit instructions: 0
32-bit instructions: 3356987
0 read port: 30869
1 read port: 1932664
2 read port: 1393454
Taken BR: 259610
Taken BR forward: 86105
Taken BR backward: 173505
Not taken BR: 211327
Not taken BR forward: 132015
Not taken BR backward: 79312
Mispredicted instructions: 120414
Mispredicted BR: 119233
Mispredicted BR taken: 78137
Mispredicted BR forward taken: 36722
Mispredicted BR backward taken: 41415
Mispredicted BR not taken: 41096
Mispredicted BR forward not taken: 15521
Mispredicted BR backward not taken: 25575
Mispredicted JALR: 358
Mispredicted CALL: 356
Mispredicted RET: 279
Partial instructions: 0
Instruction buffer full: 0
Instruction buffer dead: 852
Wait source dependency: 699990
Wait MUL unit: 94158
Wait DIV unit: 0
Wait data request: 29574
Wait data acknowledgement: 80050
Empty buffer for misaligned instructions: 0
Empty fetch port: 241681
Empty commit port: 1361920
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
Real cycles: 4087545
Real instructions: 2545397
BOOT file: /home/mrabiai/Bureau/herd-ware/sw/embench-iot/hex/SIM/WAESP32AU1V010/sglib-combined.boot8.hex
iROM file: /home/mrabiai/Bureau/herd-ware/sw/embench-iot/hex/SIM/WAESP32AU1V010/sglib-combined.irom8.hex
Simulation fast clock cycles (/1): 8484524
Simulation main clock cycles (/2): 4242262

------------------------------
           HART: 0
------------------------------
Cycles: 4242257
Time: 4242257
Retired instructions: 2640917
ALU instructions: 1861947
BRU instructions: 681422
MUL instructions: 0
DIV instructions: 9100
Load instructions: 654917
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
32-bit instructions: 2640917
0 read port: 121074
1 read port: 1438092
2 read port: 1081751
Taken BR: 223815
Taken BR forward: 95145
Taken BR backward: 128670
Not taken BR: 325663
Not taken BR forward: 212136
Not taken BR backward: 113527
Mispredicted instructions: 139445
Mispredicted BR: 121482
Mispredicted BR taken: 81918
Mispredicted BR forward taken: 41274
Mispredicted BR backward taken: 40644
Mispredicted BR not taken: 39564
Mispredicted BR forward not taken: 19068
Mispredicted BR backward not taken: 20496
Mispredicted JALR: 5143
Mispredicted CALL: 8436
Mispredicted RET: 5142
Partial instructions: 0
Instruction buffer full: 0
Instruction buffer dead: 8456
Wait source dependency: 968451
Wait MUL unit: 0
Wait DIV unit: 61694
Wait data request: 44460
Wait data acknowledgement: 83724
Empty buffer for misaligned instructions: 0
Empty fetch port: 287283
Empty commit port: 1517616
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
Real cycles: 3825586
Real instructions: 2468883
BOOT file: /home/mrabiai/Bureau/herd-ware/sw/embench-iot/hex/SIM/WAESP32AU1V010/slre.boot8.hex
iROM file: /home/mrabiai/Bureau/herd-ware/sw/embench-iot/hex/SIM/WAESP32AU1V010/slre.irom8.hex
Simulation fast clock cycles (/1): 7721650
Simulation main clock cycles (/2): 3860825

------------------------------
           HART: 0
------------------------------
Cycles: 3860820
Time: 3860820
Retired instructions: 2491616
ALU instructions: 1703343
BRU instructions: 665499
MUL instructions: 0
DIV instructions: 0
Load instructions: 467800
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
32-bit instructions: 2491616
0 read port: 119800
1 read port: 1283450
2 read port: 1088366
Taken BR: 180270
Taken BR forward: 131980
Taken BR backward: 48290
Not taken BR: 354331
Not taken BR forward: 308483
Not taken BR backward: 45848
Mispredicted instructions: 163419
Mispredicted BR: 101119
Mispredicted BR taken: 92576
Mispredicted BR forward taken: 73477
Mispredicted BR backward taken: 19099
Mispredicted BR not taken: 8543
Mispredicted BR forward not taken: 7432
Mispredicted BR backward not taken: 1111
Mispredicted JALR: 17772
Mispredicted CALL: 11773
Mispredicted RET: 17771
Partial instructions: 0
Instruction buffer full: 0
Instruction buffer dead: 32745
Wait source dependency: 680559
Wait MUL unit: 0
Wait DIV unit: 0
Wait data request: 13098
Wait data acknowledgement: 236656
Empty buffer for misaligned instructions: 0
Empty fetch port: 359584
Empty commit port: 1361763
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
[1;32mTEST REPORT: SUCCESS.[0m
Real cycles: 5811607
Real instructions: 3911670
BOOT file: /home/mrabiai/Bureau/herd-ware/sw/embench-iot/hex/SIM/WAESP32AU1V010/st.boot8.hex
iROM file: /home/mrabiai/Bureau/herd-ware/sw/embench-iot/hex/SIM/WAESP32AU1V010/st.irom8.hex
Simulation fast clock cycles (/1): 12521030
Simulation main clock cycles (/2): 6260515

------------------------------
           HART: 0
------------------------------
Cycles: 6260510
Time: 6260510
Retired instructions: 4214101
ALU instructions: 3452876
BRU instructions: 578601
MUL instructions: 146664
DIV instructions: 25760
Load instructions: 232265
Store instructions: 204062
BR instructions: 439534
BR forward instructions: 411012
BR backward instructions: 28522
JAL instructions: 94877
JALR instructions: 44190
CALL instructions: 44188
RET instructions: 44189
Read cycle instructions: 2
Cache flush instructions: 0
16-bit instructions: 0
32-bit instructions: 4214101
0 read port: 230401
1 read port: 2074323
2 read port: 1909377
Taken BR: 192349
Taken BR forward: 178857
Taken BR backward: 13492
Not taken BR: 247185
Not taken BR forward: 232155
Not taken BR backward: 15030
Mispredicted instructions: 260934
Mispredicted BR: 157800
Mispredicted BR taken: 156860
Mispredicted BR forward taken: 148070
Mispredicted BR backward taken: 8790
Mispredicted BR not taken: 940
Mispredicted BR forward not taken: 741
Mispredicted BR backward not taken: 199
Mispredicted JALR: 34738
Mispredicted CALL: 32071
Mispredicted RET: 34737
Partial instructions: 0
Instruction buffer full: 0
Instruction buffer dead: 35952
Wait source dependency: 121668
Wait MUL unit: 146664
Wait DIV unit: 741216
Wait data request: 14
Wait data acknowledgement: 71362
Empty buffer for misaligned instructions: 0
Empty fetch port: 554951
Empty commit port: 2046391
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
Real cycles: 1669503
Real instructions: 1141116
BOOT file: /home/mrabiai/Bureau/herd-ware/sw/embench-iot/hex/SIM/WAESP32AU1V010/statemate.boot8.hex
iROM file: /home/mrabiai/Bureau/herd-ware/sw/embench-iot/hex/SIM/WAESP32AU1V010/statemate.irom8.hex
Simulation fast clock cycles (/1): 3342758
Simulation main clock cycles (/2): 1671379

------------------------------
           HART: 0
------------------------------
Cycles: 1671374
Time: 1671374
Retired instructions: 1142419
ALU instructions: 756937
BRU instructions: 141670
MUL instructions: 0
DIV instructions: 0
Load instructions: 334216
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
32-bit instructions: 1142419
0 read port: 31472
1 read port: 473980
2 read port: 636967
Taken BR: 68854
Taken BR forward: 51092
Taken BR backward: 17762
Not taken BR: 37416
Not taken BR forward: 35440
Not taken BR backward: 1976
Mispredicted instructions: 57053
Mispredicted BR: 31477
Mispredicted BR taken: 29511
Mispredicted BR forward taken: 23607
Mispredicted BR backward taken: 5904
Mispredicted BR not taken: 1966
Mispredicted BR forward not taken: 0
Mispredicted BR backward not taken: 1966
Mispredicted JALR: 11802
Mispredicted CALL: 9839
Mispredicted RET: 11802
Partial instructions: 0
Instruction buffer full: 0
Instruction buffer dead: 0
Wait source dependency: 151405
Wait MUL unit: 0
Wait DIV unit: 0
Wait data request: 145408
Wait data acknowledgement: 53059
Empty buffer for misaligned instructions: 0
Empty fetch port: 114107
Empty commit port: 509301
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
Real cycles: 1755202
Real instructions: 1016017
BOOT file: /home/mrabiai/Bureau/herd-ware/sw/embench-iot/hex/SIM/WAESP32AU1V010/tarfind.boot8.hex
iROM file: /home/mrabiai/Bureau/herd-ware/sw/embench-iot/hex/SIM/WAESP32AU1V010/tarfind.irom8.hex
Simulation fast clock cycles (/1): 3595030
Simulation main clock cycles (/2): 1797515

------------------------------
           HART: 0
------------------------------
Cycles: 1797510
Time: 1797510
Retired instructions: 1042449
ALU instructions: 753382
BRU instructions: 193733
MUL instructions: 36960
DIV instructions: 36960
Load instructions: 59076
Store instructions: 206835
BR instructions: 109896
BR forward instructions: 28045
BR backward instructions: 81851
JAL instructions: 40383
JALR instructions: 43454
CALL instructions: 40332
RET instructions: 40333
Read cycle instructions: 2
Cache flush instructions: 0
16-bit instructions: 0
32-bit instructions: 1042449
0 read port: 154748
1 read port: 450074
2 read port: 437627
Taken BR: 89385
Taken BR forward: 12770
Taken BR backward: 76615
Not taken BR: 20511
Not taken BR forward: 15275
Not taken BR backward: 5236
Mispredicted instructions: 13997
Mispredicted BR: 8778
Mispredicted BR taken: 4720
Mispredicted BR forward taken: 1152
Mispredicted BR backward taken: 3568
Mispredicted BR not taken: 4058
Mispredicted BR forward not taken: 600
Mispredicted BR backward not taken: 3458
Mispredicted JALR: 5007
Mispredicted CALL: 1649
Mispredicted RET: 1886
Partial instructions: 0
Instruction buffer full: 0
Instruction buffer dead: 36919
Wait source dependency: 70901
Wait MUL unit: 36960
Wait DIV unit: 554250
Wait data request: 0
Wait data acknowledgement: 4
Empty buffer for misaligned instructions: 0
Empty fetch port: 64954
Empty commit port: 755057
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
[1;32mTEST REPORT: SUCCESS.[0m
Real cycles: 4506568
Real instructions: 3349203
BOOT file: /home/mrabiai/Bureau/herd-ware/sw/embench-iot/hex/SIM/WAESP32AU1V010/ud.boot8.hex
iROM file: /home/mrabiai/Bureau/herd-ware/sw/embench-iot/hex/SIM/WAESP32AU1V010/ud.irom8.hex
Simulation fast clock cycles (/1): 9022094
Simulation main clock cycles (/2): 4511047

------------------------------
           HART: 0
------------------------------
Cycles: 4511042
Time: 4511042
Retired instructions: 3352562
ALU instructions: 2586233
BRU instructions: 597715
MUL instructions: 128673
DIV instructions: 31059
Load instructions: 439364
Store instructions: 210536
BR instructions: 480843
BR forward instructions: 201175
BR backward instructions: 279668
JAL instructions: 79883
JALR instructions: 36989
CALL instructions: 36988
RET instructions: 36989
Read cycle instructions: 2
Cache flush instructions: 0
16-bit instructions: 0
32-bit instructions: 3352562
0 read port: 130187
1 read port: 1813650
2 read port: 1408725
Taken BR: 281146
Taken BR forward: 97617
Taken BR backward: 183529
Not taken BR: 199697
Not taken BR forward: 103558
Not taken BR backward: 96139
Mispredicted instructions: 158340
Mispredicted BR: 137588
Mispredicted BR taken: 85822
Mispredicted BR forward taken: 19249
Mispredicted BR backward taken: 66573
Mispredicted BR not taken: 51766
Mispredicted BR forward not taken: 0
Mispredicted BR backward not taken: 51766
Mispredicted JALR: 13329
Mispredicted CALL: 2976
Mispredicted RET: 13329
Partial instructions: 0
Instruction buffer full: 0
Instruction buffer dead: 10353
Wait source dependency: 476310
Wait MUL unit: 128673
Wait DIV unit: 124236
Wait data request: 0
Wait data acknowledgement: 63601
Empty buffer for misaligned instructions: 0
Empty fetch port: 328513
Empty commit port: 1156997
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
[1;32mTEST REPORT: SUCCESS.[0m
Real cycles: 1943770
Real instructions: 1254751
BOOT file: /home/mrabiai/Bureau/herd-ware/sw/embench-iot/hex/SIM/WAESP32AU1V010/wikisort.boot8.hex
iROM file: /home/mrabiai/Bureau/herd-ware/sw/embench-iot/hex/SIM/WAESP32AU1V010/wikisort.irom8.hex
Simulation fast clock cycles (/1): 7799624
Simulation main clock cycles (/2): 3899812

------------------------------
           HART: 0
------------------------------
Cycles: 3899807
Time: 3899807
Retired instructions: 2519061
ALU instructions: 2014793
BRU instructions: 422350
MUL instructions: 58400
DIV instructions: 19308
Load instructions: 386541
Store instructions: 224238
BR instructions: 265300
BR forward instructions: 192682
BR backward instructions: 72618
JAL instructions: 41273
JALR instructions: 115777
CALL instructions: 68989
RET instructions: 68990
Read cycle instructions: 2
Cache flush instructions: 0
16-bit instructions: 0
32-bit instructions: 2519061
0 read port: 97577
1 read port: 1462769
2 read port: 958715
Taken BR: 145187
Taken BR forward: 84889
Taken BR backward: 60298
Not taken BR: 120113
Not taken BR forward: 107793
Not taken BR backward: 12320
Mispredicted instructions: 141427
Mispredicted BR: 82762
Mispredicted BR taken: 79481
Mispredicted BR forward taken: 71335
Mispredicted BR backward taken: 8146
Mispredicted BR not taken: 3281
Mispredicted BR forward not taken: 1071
Mispredicted BR backward not taken: 2210
Mispredicted JALR: 24489
Mispredicted CALL: 21262
Mispredicted RET: 21832
Partial instructions: 0
Instruction buffer full: 0
Instruction buffer dead: 23492
Wait source dependency: 216001
Wait MUL unit: 58400
Wait DIV unit: 538940
Wait data request: 72
Wait data acknowledgement: 47700
Empty buffer for misaligned instructions: 0
Empty fetch port: 303965
Empty commit port: 1362460
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
