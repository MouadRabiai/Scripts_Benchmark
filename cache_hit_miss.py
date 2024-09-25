import re

def extract_cache_stats(report):

    exec_blocks = re.findall(
        r"EXEC NAME: (.+?)\n.*?L1I hits: (\d+).*?L1I misses: (\d+).*?L1D hits: (\d+).*?L1D misses: (\d+).*?L2 hits: (\d+).*?L2 misses: (\d+)",
        report, re.DOTALL)


    global_l1i_hits = 0
    global_l1i_misses = 0
    global_l1d_hits = 0
    global_l1d_misses = 0
    global_l2_hits = 0
    global_l2_misses = 0

    for exec_name, l1i_hits, l1i_misses, l1d_hits, l1d_misses, l2_hits, l2_misses in exec_blocks:

        l1i_hits = int(l1i_hits)
        l1i_misses = int(l1i_misses)
        l1d_hits = int(l1d_hits)
        l1d_misses = int(l1d_misses)
        l2_hits = int(l2_hits)
        l2_misses = int(l2_misses)


        total_hits = l1i_hits + l1d_hits + l2_hits
        total_misses = l1i_misses + l1d_misses + l2_misses

        print(f"Programme: {exec_name}")
        print(f"  Total hits: {total_hits}")
        print(f"  Total misses: {total_misses}")
        print("\n")

report_data = """
EXEC NAME: aha-mont64
[1;32mTEST REPORT: SUCCESS.[0m
Real cycles: 5538013
Real instructions: 4531262
BOOT file: /home/mrabiai/Bureau/herd-ware/sw/embench-iot/hex/SIM/WAESP32AU1V210/aha-mont64.boot8.hex
iROM file: /home/mrabiai/Bureau/herd-ware/sw/embench-iot/hex/SIM/WAESP32AU1V210/aha-mont64.irom8.hex
Simulation fast clock cycles (/1): 11104678
Simulation main clock cycles (/2): 5552339

------------------------------
           HART: 0
------------------------------
Cycles: 5552334
Time: 5552334
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
Mispredicted instructions: 153216
Mispredicted BR: 150013
Mispredicted BR taken: 107603
Mispredicted BR forward taken: 72402
Mispredicted BR backward taken: 35201
Mispredicted BR not taken: 42410
Mispredicted BR forward not taken: 34882
Mispredicted BR backward not taken: 7528
Mispredicted JALR: 434
Mispredicted CALL: 1284
Mispredicted RET: 434
Partial instructions: 0
Instruction buffer full: 0
Instruction buffer dead: 2
Wait source dependency: 2131
Wait MUL unit: 35632
Wait DIV unit: 0
Wait data request: 533
Wait data acknowledgement: 29
Empty buffer for misaligned instructions: 0
Empty fetch port: 673881
Empty commit port: 1010102
L1I hits: 4971735
L1I misses: 24647
L1I prefetches: 0
L1D hits: 12403
L1D misses: 7
L1D prefetches: 0
L2 hits: 76565
L2 misses: 24644
L2 prefetches: 0
------------------------------

EXEC NAME: crc32
[1;32mTEST REPORT: SUCCESS.[0m
Real cycles: 4439041
Real instructions: 3831161
BOOT file: /home/mrabiai/Bureau/herd-ware/sw/embench-iot/hex/SIM/WAESP32AU1V210/crc32.boot8.hex
iROM file: /home/mrabiai/Bureau/herd-ware/sw/embench-iot/hex/SIM/WAESP32AU1V210/crc32.irom8.hex
Simulation fast clock cycles (/1): 8933184
Simulation main clock cycles (/2): 4466592

------------------------------
           HART: 0
------------------------------
Cycles: 4466587
Time: 4466587
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
Mispredicted instructions: 6448
Mispredicted BR: 6419
Mispredicted BR taken: 6247
Mispredicted BR forward taken: 1
Mispredicted BR backward taken: 6246
Mispredicted BR not taken: 172
Mispredicted BR forward not taken: 0
Mispredicted BR backward not taken: 172
Mispredicted JALR: 12
Mispredicted CALL: 14
Mispredicted RET: 12
Partial instructions: 0
Instruction buffer full: 0
Instruction buffer dead: 5507
Wait source dependency: 411259
Wait MUL unit: 175104
Wait DIV unit: 0
Wait data request: 41
Wait data acknowledgement: 61091
Empty buffer for misaligned instructions: 0
Empty fetch port: 18891
Empty commit port: 612689
L1I hits: 3873216
L1I misses: 30
L1I prefetches: 0
L1D hits: 520020
L1D misses: 5511
L1D prefetches: 0
L2 hits: 195001
L2 misses: 2464
L2 prefetches: 0
------------------------------

EXEC NAME: cubic
[1;32mTEST REPORT: SUCCESS.[0m
Real cycles: 23602841
Real instructions: 7079338
BOOT file: /home/mrabiai/Bureau/herd-ware/sw/embench-iot/hex/SIM/WAESP32AU1V210/cubic.boot8.hex
iROM file: /home/mrabiai/Bureau/herd-ware/sw/embench-iot/hex/SIM/WAESP32AU1V210/cubic.irom8.hex
Simulation fast clock cycles (/1): 51936740
Simulation main clock cycles (/2): 25968370

------------------------------
           HART: 0
------------------------------
Cycles: 25968365
Time: 25968365
Retired instructions: 7788415
ALU instructions: 6407745
BRU instructions: 975663
MUL instructions: 372746
DIV instructions: 27368
Load instructions: 667911
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
32-bit instructions: 7788415
0 read port: 331814
1 read port: 3545917
2 read port: 3910684
Taken BR: 421917
Taken BR forward: 311327
Taken BR backward: 110590
Not taken BR: 393805
Not taken BR forward: 330940
Not taken BR backward: 62865
Mispredicted instructions: 530651
Mispredicted BR: 385482
Mispredicted BR taken: 327396
Mispredicted BR forward taken: 267105
Mispredicted BR backward taken: 60291
Mispredicted BR not taken: 58086
Mispredicted BR forward not taken: 35504
Mispredicted BR backward not taken: 22582
Mispredicted JALR: 42027
Mispredicted CALL: 47493
Mispredicted RET: 41784
Partial instructions: 0
Instruction buffer full: 0
Instruction buffer dead: 22134
Wait source dependency: 292695
Wait MUL unit: 372746
Wait DIV unit: 563024
Wait data request: 362347
Wait data acknowledgement: 112765
Empty buffer for misaligned instructions: 0
Empty fetch port: 16131456
Empty commit port: 18179950
L1I hits: 8161906
L1I misses: 981273
L1I prefetches: 0
L1D hits: 1273241
L1D misses: 6130
L1D prefetches: 0
L2 hits: 3560052
L2 misses: 868286
L2 prefetches: 0
------------------------------

EXEC NAME: edn
[1;32mTEST REPORT: SUCCESS.[0m
Real cycles: 4765758
Real instructions: 3919331
BOOT file: /home/mrabiai/Bureau/herd-ware/sw/embench-iot/hex/SIM/WAESP32AU1V210/edn.boot8.hex
iROM file: /home/mrabiai/Bureau/herd-ware/sw/embench-iot/hex/SIM/WAESP32AU1V210/edn.irom8.hex
Simulation fast clock cycles (/1): 9656422
Simulation main clock cycles (/2): 4828211

------------------------------
           HART: 0
------------------------------
Cycles: 4828206
Time: 4828206
Retired instructions: 3967193
ALU instructions: 2185285
BRU instructions: 360606
MUL instructions: 580008
DIV instructions: 0
Load instructions: 1331378
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
32-bit instructions: 3967193
0 read port: 571
1 read port: 2246984
2 read port: 1719638
Taken BR: 348304
Taken BR forward: 92
Taken BR backward: 348212
Not taken BR: 11478
Not taken BR forward: 297
Not taken BR backward: 11181
Mispredicted instructions: 22742
Mispredicted BR: 22611
Mispredicted BR taken: 11344
Mispredicted BR forward taken: 92
Mispredicted BR backward taken: 11252
Mispredicted BR not taken: 11267
Mispredicted BR forward not taken: 87
Mispredicted BR backward not taken: 11180
Mispredicted JALR: 20
Mispredicted CALL: 105
Mispredicted RET: 20
Partial instructions: 0
Instruction buffer full: 0
Instruction buffer dead: 11925
Wait source dependency: 641470
Wait MUL unit: 580008
Wait DIV unit: 0
Wait data request: 165172
Wait data acknowledgement: 95956
Empty buffer for misaligned instructions: 0
Empty fetch port: 111050
Empty commit port: 861013
L1I hits: 3617696
L1I misses: 3961
L1I prefetches: 0
L1D hits: 1005046
L1D misses: 12508
L1D prefetches: 0
L2 hits: 160992
L2 misses: 12522
L2 prefetches: 0
------------------------------

EXEC NAME: huffbench
[1;32mTEST REPORT: SUCCESS.[0m
Real cycles: 3743632
Real instructions: 2598468
BOOT file: /home/mrabiai/Bureau/herd-ware/sw/embench-iot/hex/SIM/WAESP32AU1V210/huffbench.boot8.hex
iROM file: /home/mrabiai/Bureau/herd-ware/sw/embench-iot/hex/SIM/WAESP32AU1V210/huffbench.irom8.hex
Simulation fast clock cycles (/1): 8201692
Simulation main clock cycles (/2): 4100846

------------------------------
           HART: 0
------------------------------
Cycles: 4100841
Time: 4100841
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
Mispredicted instructions: 163150
Mispredicted BR: 162692
Mispredicted BR taken: 122426
Mispredicted BR forward taken: 44287
Mispredicted BR backward taken: 78139
Mispredicted BR not taken: 40266
Mispredicted BR forward not taken: 25920
Mispredicted BR backward not taken: 14346
Mispredicted JALR: 146
Mispredicted CALL: 169
Mispredicted RET: 133
Partial instructions: 0
Instruction buffer full: 0
Instruction buffer dead: 7763
Wait source dependency: 627791
Wait MUL unit: 0
Wait DIV unit: 0
Wait data request: 124701
Wait data acknowledgement: 47430
Empty buffer for misaligned instructions: 0
Empty fetch port: 349387
Empty commit port: 1260563
L1I hits: 3173788
L1I misses: 1200
L1I prefetches: 0
L1D hits: 697310
L1D misses: 4931
L1D prefetches: 0
L2 hits: 229442
L2 misses: 5463
L2 prefetches: 0
------------------------------

EXEC NAME: matmult-int
[1;32mTEST REPORT: SUCCESS.[0m
Real cycles: 5113111
Real instructions: 3183124
BOOT file: /home/mrabiai/Bureau/herd-ware/sw/embench-iot/hex/SIM/WAESP32AU1V210/matmult-int.boot8.hex
iROM file: /home/mrabiai/Bureau/herd-ware/sw/embench-iot/hex/SIM/WAESP32AU1V210/matmult-int.irom8.hex
Simulation fast clock cycles (/1): 10535918
Simulation main clock cycles (/2): 5267959

------------------------------
           HART: 0
------------------------------
Cycles: 5267954
Time: 5267954
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
Mispredicted instructions: 40019
Mispredicted BR: 39987
Mispredicted BR taken: 20060
Mispredicted BR forward taken: 3
Mispredicted BR backward taken: 20057
Mispredicted BR not taken: 19927
Mispredicted BR forward not taken: 1
Mispredicted BR backward not taken: 19926
Mispredicted JALR: 13
Mispredicted CALL: 15
Mispredicted RET: 13
Partial instructions: 0
Instruction buffer full: 0
Instruction buffer dead: 79167
Wait source dependency: 1571231
Wait MUL unit: 376000
Wait DIV unit: 15945
Wait data request: 246389
Wait data acknowledgement: 955010
Empty buffer for misaligned instructions: 0
Empty fetch port: 88456
Empty commit port: 2001154
L1I hits: 3465926
L1I misses: 57
L1I prefetches: 0
L1D hits: 1148003
L1D misses: 78223
L1D prefetches: 0
L2 hits: 688323
L2 misses: 56056
L2 prefetches: 0
------------------------------

EXEC NAME: md5sum
[1;32mTEST REPORT: SUCCESS.[0m
Real cycles: 2449100
Real instructions: 2046782
BOOT file: /home/mrabiai/Bureau/herd-ware/sw/embench-iot/hex/SIM/WAESP32AU1V210/md5sum.boot8.hex
iROM file: /home/mrabiai/Bureau/herd-ware/sw/embench-iot/hex/SIM/WAESP32AU1V210/md5sum.irom8.hex
Simulation fast clock cycles (/1): 5011272
Simulation main clock cycles (/2): 2505636

------------------------------
           HART: 0
------------------------------
Cycles: 2505631
Time: 2505631
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
Mispredicted instructions: 28875
Mispredicted BR: 27791
Mispredicted BR taken: 25696
Mispredicted BR forward taken: 11026
Mispredicted BR backward taken: 14670
Mispredicted BR not taken: 2095
Mispredicted BR forward not taken: 1729
Mispredicted BR backward not taken: 366
Mispredicted JALR: 482
Mispredicted CALL: 415
Mispredicted RET: 429
Partial instructions: 0
Instruction buffer full: 0
Instruction buffer dead: 11371
Wait source dependency: 80836
Wait MUL unit: 52
Wait DIV unit: 0
Wait data request: 189079
Wait data acknowledgement: 85772
Empty buffer for misaligned instructions: 0
Empty fetch port: 100232
Empty commit port: 416115
L1I hits: 2184041
L1I misses: 2440
L1I prefetches: 0
L1D hits: 259644
L1D misses: 8795
L1D prefetches: 0
L2 hits: 131182
L2 misses: 9527
L2 prefetches: 0
------------------------------

EXEC NAME: minver
[1;32mTEST REPORT: SUCCESS.[0m
Real cycles: 15564386
Real instructions: 4929591
BOOT file: /home/mrabiai/Bureau/herd-ware/sw/embench-iot/hex/SIM/WAESP32AU1V210/minver.boot8.hex
iROM file: /home/mrabiai/Bureau/herd-ware/sw/embench-iot/hex/SIM/WAESP32AU1V210/minver.irom8.hex
Simulation fast clock cycles (/1): 31199024
Simulation main clock cycles (/2): 15599512

------------------------------
           HART: 0
------------------------------
Cycles: 15599507
Time: 15599507
Retired instructions: 4941225
ALU instructions: 3909806
BRU instructions: 920210
MUL instructions: 73392
DIV instructions: 35584
Load instructions: 422808
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
32-bit instructions: 4941225
0 read port: 297666
1 read port: 2735498
2 read port: 1908061
Taken BR: 332220
Taken BR forward: 289355
Taken BR backward: 42865
Not taken BR: 381528
Not taken BR forward: 340913
Not taken BR backward: 40615
Mispredicted instructions: 445065
Mispredicted BR: 290836
Mispredicted BR taken: 255892
Mispredicted BR forward taken: 218610
Mispredicted BR backward taken: 37282
Mispredicted BR not taken: 34944
Mispredicted BR forward not taken: 22153
Mispredicted BR backward not taken: 12791
Mispredicted JALR: 32557
Mispredicted CALL: 59346
Mispredicted RET: 32001
Partial instructions: 0
Instruction buffer full: 0
Instruction buffer dead: 32768
Wait source dependency: 96967
Wait MUL unit: 73392
Wait DIV unit: 879592
Wait data request: 140559
Wait data acknowledgement: 2939
Empty buffer for misaligned instructions: 0
Empty fetch port: 8837479
Empty commit port: 10658282
L1I hits: 5563886
L1I misses: 561614
L1I prefetches: 0
L1D hits: 806094
L1D misses: 18
L1D prefetches: 0
L2 hits: 2133405
L2 misses: 456295
L2 prefetches: 0
------------------------------

EXEC NAME: nbody
[1;32mTEST REPORT: SUCCESS.[0m
Real cycles: 10742874
Real instructions: 3475621
BOOT file: /home/mrabiai/Bureau/herd-ware/sw/embench-iot/hex/SIM/WAESP32AU1V210/nbody.boot8.hex
iROM file: /home/mrabiai/Bureau/herd-ware/sw/embench-iot/hex/SIM/WAESP32AU1V210/nbody.irom8.hex
Simulation fast clock cycles (/1): 43008214
Simulation main clock cycles (/2): 21504107

------------------------------
           HART: 0
------------------------------
Cycles: 21504102
Time: 21504102
Retired instructions: 6955185
ALU instructions: 5595361
BRU instructions: 1107242
MUL instructions: 232756
DIV instructions: 16216
Load instructions: 347587
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
32-bit instructions: 6955185
0 read port: 291512
1 read port: 3386958
2 read port: 3276715
Taken BR: 450164
Taken BR forward: 300844
Taken BR backward: 149320
Not taken BR: 488509
Not taken BR forward: 412039
Not taken BR backward: 76470
Mispredicted instructions: 530310
Mispredicted BR: 378322
Mispredicted BR taken: 301287
Mispredicted BR forward taken: 234199
Mispredicted BR backward taken: 67088
Mispredicted BR not taken: 77035
Mispredicted BR forward not taken: 57424
Mispredicted BR backward not taken: 19611
Mispredicted JALR: 41794
Mispredicted CALL: 46943
Mispredicted RET: 41790
Partial instructions: 0
Instruction buffer full: 0
Instruction buffer dead: 17622
Wait source dependency: 42015
Wait MUL unit: 232756
Wait DIV unit: 480422
Wait data request: 94922
Wait data acknowledgement: 2840
Empty buffer for misaligned instructions: 0
Empty fetch port: 12999894
Empty commit port: 14548917
L1I hits: 7506879
L1I misses: 810303
L1I prefetches: 0
L1D hits: 621312
L1D misses: 69
L1D prefetches: 0
L2 hits: 2733229
L2 misses: 739944
L2 prefetches: 0
------------------------------

EXEC NAME: nettle-aes
[1;32mTEST REPORT: SUCCESS.[0m
Real cycles: 12254954
Real instructions: 4432637
BOOT file: /home/mrabiai/Bureau/herd-ware/sw/embench-iot/hex/SIM/WAESP32AU1V210/nettle-aes.boot8.hex
iROM file: /home/mrabiai/Bureau/herd-ware/sw/embench-iot/hex/SIM/WAESP32AU1V210/nettle-aes.irom8.hex
Simulation fast clock cycles (/1): 24842726
Simulation main clock cycles (/2): 12421363

------------------------------
           HART: 0
------------------------------
Cycles: 12421358
Time: 12421358
Retired instructions: 4495336
ALU instructions: 4325729
BRU instructions: 78934
MUL instructions: 0
DIV instructions: 8216
Load instructions: 846122
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
32-bit instructions: 4495336
0 read port: 2087
1 read port: 3081398
2 read port: 1411851
Taken BR: 48867
Taken BR forward: 239
Taken BR backward: 48628
Not taken BR: 29011
Not taken BR forward: 10283
Not taken BR backward: 18728
Mispredicted instructions: 24300
Mispredicted BR: 23399
Mispredicted BR taken: 15314
Mispredicted BR forward taken: 239
Mispredicted BR backward taken: 15075
Mispredicted BR not taken: 8085
Mispredicted BR forward not taken: 236
Mispredicted BR backward not taken: 7849
Mispredicted JALR: 254
Mispredicted CALL: 407
Mispredicted RET: 253
Partial instructions: 0
Instruction buffer full: 0
Instruction buffer dead: 469112
Wait source dependency: 76457
Wait MUL unit: 0
Wait DIV unit: 52456
Wait data request: 3660072
Wait data acknowledgement: 7035122
Empty buffer for misaligned instructions: 0
Empty fetch port: 985025
Empty commit port: 7926022
L1I hits: 4955094
L1I misses: 42047
L1I prefetches: 0
L1D hits: 401378
L1D misses: 479457
L1D prefetches: 0
L2 hits: 1652496
L2 misses: 492077
L2 prefetches: 0
------------------------------

EXEC NAME: nettle-sha256
[1;32mTEST REPORT: SUCCESS.[0m
Real cycles: 11378637
Real instructions: 4016185
BOOT file: /home/mrabiai/Bureau/herd-ware/sw/embench-iot/hex/SIM/WAESP32AU1V210/nettle-sha256.boot8.hex
iROM file: /home/mrabiai/Bureau/herd-ware/sw/embench-iot/hex/SIM/WAESP32AU1V210/nettle-sha256.irom8.hex
Simulation fast clock cycles (/1): 22810226
Simulation main clock cycles (/2): 11405113

------------------------------
           HART: 0
------------------------------
Cycles: 11405108
Time: 11405108
Retired instructions: 4025354
ALU instructions: 3908618
BRU instructions: 48168
MUL instructions: 0
DIV instructions: 0
Load instructions: 423338
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
32-bit instructions: 4025354
0 read port: 8122
1 read port: 1791561
2 read port: 2225671
Taken BR: 27175
Taken BR forward: 3333
Taken BR backward: 23842
Not taken BR: 11444
Not taken BR forward: 5250
Not taken BR backward: 6194
Mispredicted instructions: 24042
Mispredicted BR: 14494
Mispredicted BR taken: 10398
Mispredicted BR forward taken: 3333
Mispredicted BR backward taken: 7065
Mispredicted BR not taken: 4096
Mispredicted BR forward not taken: 956
Mispredicted BR backward not taken: 3140
Mispredicted JALR: 3821
Mispredicted CALL: 3344
Mispredicted RET: 3344
Partial instructions: 0
Instruction buffer full: 0
Instruction buffer dead: 49
Wait source dependency: 66994
Wait MUL unit: 0
Wait DIV unit: 0
Wait data request: 67305
Wait data acknowledgement: 15959
Empty buffer for misaligned instructions: 0
Empty fetch port: 7250273
Empty commit port: 7379754
L1I hits: 3587193
L1I misses: 471453
L1I prefetches: 0
L1D hits: 554865
L1D misses: 41
L1D prefetches: 0
L2 hits: 1560220
L2 misses: 452507
L2 prefetches: 0
------------------------------

EXEC NAME: nsichneu
[1;32mTEST REPORT: SUCCESS.[0m
Real cycles: 12241225
Real instructions: 2236758
BOOT file: /home/mrabiai/Bureau/herd-ware/sw/embench-iot/hex/SIM/WAESP32AU1V210/nsichneu.boot8.hex
iROM file: /home/mrabiai/Bureau/herd-ware/sw/embench-iot/hex/SIM/WAESP32AU1V210/nsichneu.irom8.hex
Simulation fast clock cycles (/1): 24505184
Simulation main clock cycles (/2): 12252592

------------------------------
           HART: 0
------------------------------
Cycles: 12252587
Time: 12252587
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
Mispredicted instructions: 444797
Mispredicted BR: 208224
Mispredicted BR taken: 186039
Mispredicted BR forward taken: 147843
Mispredicted BR backward taken: 38196
Mispredicted BR not taken: 22185
Mispredicted BR forward not taken: 17253
Mispredicted BR backward not taken: 4932
Mispredicted JALR: 14
Mispredicted CALL: 12
Mispredicted RET: 13
Partial instructions: 0
Instruction buffer full: 0
Instruction buffer dead: 3
Wait source dependency: 2177010
Wait MUL unit: 0
Wait DIV unit: 0
Wait data request: 1327
Wait data acknowledgement: 26
Empty buffer for misaligned instructions: 0
Empty fetch port: 7351085
Empty commit port: 10013639
L1I hits: 2677606
L1I misses: 491624
L1I prefetches: 0
L1D hits: 1230855
L1D misses: 7
L1D prefetches: 0
L2 hits: 1476174
L2 misses: 494091
L2 prefetches: 0
------------------------------

EXEC NAME: picojpeg
[1;32mTEST REPORT: SUCCESS.[0m
Real cycles: 6439423
Real instructions: 4092516
BOOT file: /home/mrabiai/Bureau/herd-ware/sw/embench-iot/hex/SIM/WAESP32AU1V210/picojpeg.boot8.hex
iROM file: /home/mrabiai/Bureau/herd-ware/sw/embench-iot/hex/SIM/WAESP32AU1V210/picojpeg.irom8.hex
Simulation fast clock cycles (/1): 15012944
Simulation main clock cycles (/2): 7506472

------------------------------
           HART: 0
------------------------------
Cycles: 7506467
Time: 7506467
Retired instructions: 4776087
ALU instructions: 3679134
BRU instructions: 478978
MUL instructions: 123116
DIV instructions: 0
Load instructions: 1000773
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
32-bit instructions: 4776087
0 read port: 65915
1 read port: 3002411
2 read port: 1707761
Taken BR: 318375
Taken BR forward: 154581
Taken BR backward: 163794
Not taken BR: 83167
Not taken BR forward: 64208
Not taken BR backward: 18959
Mispredicted instructions: 129214
Mispredicted BR: 103494
Mispredicted BR taken: 92541
Mispredicted BR forward taken: 64796
Mispredicted BR backward taken: 27745
Mispredicted BR not taken: 10953
Mispredicted BR forward not taken: 7975
Mispredicted BR backward not taken: 2978
Mispredicted JALR: 7118
Mispredicted CALL: 8027
Mispredicted RET: 5921
Partial instructions: 0
Instruction buffer full: 0
Instruction buffer dead: 11337
Wait source dependency: 384777
Wait MUL unit: 123116
Wait DIV unit: 0
Wait data request: 415519
Wait data acknowledgement: 252987
Empty buffer for misaligned instructions: 0
Empty fetch port: 1852273
Empty commit port: 2730380
L1I hits: 4684601
L1I misses: 105108
L1I prefetches: 0
L1D hits: 1210237
L1D misses: 15885
L1D prefetches: 0
L2 hits: 943097
L2 misses: 105629
L2 prefetches: 0
------------------------------

EXEC NAME: primecount
[1;32mTEST REPORT: SUCCESS.[0m
Real cycles: 4079191
Real instructions: 2148524
BOOT file: /home/mrabiai/Bureau/herd-ware/sw/embench-iot/hex/SIM/WAESP32AU1V210/primecount.boot8.hex
iROM file: /home/mrabiai/Bureau/herd-ware/sw/embench-iot/hex/SIM/WAESP32AU1V210/primecount.irom8.hex
Simulation fast clock cycles (/1): 16318270
Simulation main clock cycles (/2): 8159135

------------------------------
           HART: 0
------------------------------
Cycles: 8159130
Time: 8159130
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
Mispredicted instructions: 369056
Mispredicted BR: 369028
Mispredicted BR taken: 299388
Mispredicted BR forward taken: 173565
Mispredicted BR backward taken: 125823
Mispredicted BR not taken: 69640
Mispredicted BR forward not taken: 69634
Mispredicted BR backward not taken: 6
Mispredicted JALR: 11
Mispredicted CALL: 13
Mispredicted RET: 11
Partial instructions: 0
Instruction buffer full: 0
Instruction buffer dead: 6
Wait source dependency: 2319502
Wait MUL unit: 131516
Wait DIV unit: 0
Wait data request: 109
Wait data acknowledgement: 4
Empty buffer for misaligned instructions: 0
Empty fetch port: 738585
Empty commit port: 3861922
L1I hits: 5404346
L1I misses: 31
L1I prefetches: 0
L1D hits: 870935
L1D misses: 13
L1D prefetches: 0
L2 hits: 119867
L2 misses: 39
L2 prefetches: 0
------------------------------

EXEC NAME: qrduino
[1;32mTEST REPORT: SUCCESS.[0m
Real cycles: 4069805
Real instructions: 3151733
BOOT file: /home/mrabiai/Bureau/herd-ware/sw/embench-iot/hex/SIM/WAESP32AU1V210/qrduino.boot8.hex
iROM file: /home/mrabiai/Bureau/herd-ware/sw/embench-iot/hex/SIM/WAESP32AU1V210/qrduino.irom8.hex
Simulation fast clock cycles (/1): 9788152
Simulation main clock cycles (/2): 4894076

------------------------------
           HART: 0
------------------------------
Cycles: 4894071
Time: 4894071
Retired instructions: 3786688
ALU instructions: 2748361
BRU instructions: 501206
MUL instructions: 94158
DIV instructions: 0
Load instructions: 1034345
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
32-bit instructions: 3786688
0 read port: 30869
1 read port: 2362365
2 read port: 1393454
Taken BR: 259610
Taken BR forward: 86105
Taken BR backward: 173505
Not taken BR: 211327
Not taken BR forward: 132015
Not taken BR backward: 79312
Mispredicted instructions: 163745
Mispredicted BR: 162547
Mispredicted BR taken: 122552
Mispredicted BR forward taken: 45796
Mispredicted BR backward taken: 76756
Mispredicted BR not taken: 39995
Mispredicted BR forward not taken: 18187
Mispredicted BR backward not taken: 21808
Mispredicted JALR: 375
Mispredicted CALL: 356
Mispredicted RET: 296
Partial instructions: 0
Instruction buffer full: 0
Instruction buffer dead: 555
Wait source dependency: 650982
Wait MUL unit: 94158
Wait DIV unit: 0
Wait data request: 40226
Wait data acknowledgement: 3243
Empty buffer for misaligned instructions: 0
Empty fetch port: 398171
Empty commit port: 1107383
L1I hits: 3842550
L1I misses: 4668
L1I prefetches: 0
L1D hits: 687402
L1D misses: 282
L1D prefetches: 0
L2 hits: 98730
L2 misses: 4741
L2 prefetches: 0
------------------------------

EXEC NAME: sglib-combined
[1;32mTEST REPORT: SUCCESS.[0m
Real cycles: 4513168
Real instructions: 2622218
BOOT file: /home/mrabiai/Bureau/herd-ware/sw/embench-iot/hex/SIM/WAESP32AU1V210/sglib-combined.boot8.hex
iROM file: /home/mrabiai/Bureau/herd-ware/sw/embench-iot/hex/SIM/WAESP32AU1V210/sglib-combined.irom8.hex
Simulation fast clock cycles (/1): 9388752
Simulation main clock cycles (/2): 4694376

------------------------------
           HART: 0
------------------------------
Cycles: 4694371
Time: 4694371
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
Mispredicted instructions: 171093
Mispredicted BR: 152707
Mispredicted BR taken: 110974
Mispredicted BR forward taken: 54846
Mispredicted BR backward taken: 56128
Mispredicted BR not taken: 41733
Mispredicted BR forward not taken: 20264
Mispredicted BR backward not taken: 21469
Mispredicted JALR: 5238
Mispredicted CALL: 8681
Mispredicted RET: 5237
Partial instructions: 0
Instruction buffer full: 0
Instruction buffer dead: 27950
Wait source dependency: 1128116
Wait MUL unit: 0
Wait DIV unit: 61694
Wait data request: 181062
Wait data acknowledgement: 238227
Empty buffer for misaligned instructions: 0
Empty fetch port: 422325
Empty commit port: 1973984
L1I hits: 3167131
L1I misses: 3466
L1I prefetches: 0
L1D hits: 954668
L1D misses: 22421
L1D prefetches: 0
L2 hits: 403233
L2 misses: 21985
L2 prefetches: 0
------------------------------

EXEC NAME: slre
[1;32mTEST REPORT: SUCCESS.[0m
Real cycles: 5938795
Real instructions: 2590543
BOOT file: /home/mrabiai/Bureau/herd-ware/sw/embench-iot/hex/SIM/WAESP32AU1V210/slre.boot8.hex
iROM file: /home/mrabiai/Bureau/herd-ware/sw/embench-iot/hex/SIM/WAESP32AU1V210/slre.irom8.hex
Simulation fast clock cycles (/1): 11987466
Simulation main clock cycles (/2): 5993733

------------------------------
           HART: 0
------------------------------
Cycles: 5993728
Time: 5993728
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
Mispredicted instructions: 210443
Mispredicted BR: 144338
Mispredicted BR taken: 130487
Mispredicted BR forward taken: 95786
Mispredicted BR backward taken: 34701
Mispredicted BR not taken: 13851
Mispredicted BR forward not taken: 12856
Mispredicted BR backward not taken: 995
Mispredicted JALR: 20353
Mispredicted CALL: 11258
Mispredicted RET: 20352
Partial instructions: 0
Instruction buffer full: 0
Instruction buffer dead: 3482
Wait source dependency: 466468
Wait MUL unit: 0
Wait DIV unit: 0
Wait data request: 168752
Wait data acknowledgement: 32266
Empty buffer for misaligned instructions: 0
Empty fetch port: 2494248
Empty commit port: 3379346
L1I hits: 2939885
L1I misses: 140018
L1I prefetches: 0
L1D hits: 764517
L1D misses: 695
L1D prefetches: 0
L2 hits: 719198
L2 misses: 122444
L2 prefetches: 0
------------------------------

EXEC NAME: st
[1;32mTEST REPORT: SUCCESS.[0m
Real cycles: 14818061
Real instructions: 3921135
BOOT file: /home/mrabiai/Bureau/herd-ware/sw/embench-iot/hex/SIM/WAESP32AU1V210/st.boot8.hex
iROM file: /home/mrabiai/Bureau/herd-ware/sw/embench-iot/hex/SIM/WAESP32AU1V210/st.irom8.hex
Simulation fast clock cycles (/1): 31927510
Simulation main clock cycles (/2): 15963755

------------------------------
           HART: 0
------------------------------
Cycles: 15963750
Time: 15963750
Retired instructions: 4224293
ALU instructions: 3463068
BRU instructions: 578601
MUL instructions: 146664
DIV instructions: 25760
Load instructions: 242457
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
32-bit instructions: 4224293
0 read port: 230401
1 read port: 2084515
2 read port: 1909377
Taken BR: 192349
Taken BR forward: 178857
Taken BR backward: 13492
Not taken BR: 247185
Not taken BR forward: 232155
Not taken BR backward: 15030
Mispredicted instructions: 301013
Mispredicted BR: 192976
Mispredicted BR taken: 172972
Mispredicted BR forward taken: 162430
Mispredicted BR backward taken: 10542
Mispredicted BR not taken: 20004
Mispredicted BR forward not taken: 17601
Mispredicted BR backward not taken: 2403
Mispredicted JALR: 29450
Mispredicted CALL: 38227
Mispredicted RET: 29449
Partial instructions: 0
Instruction buffer full: 0
Instruction buffer dead: 26370
Wait source dependency: 57431
Wait MUL unit: 146664
Wait DIV unit: 749280
Wait data request: 97322
Wait data acknowledgement: 24234
Empty buffer for misaligned instructions: 0
Empty fetch port: 10405224
Empty commit port: 11739457
L1I hits: 4333198
L1I misses: 665972
L1I prefetches: 0
L1D hits: 434042
L1D misses: 2185
L1D prefetches: 0
L2 hits: 2228847
L2 misses: 597213
L2 prefetches: 0
------------------------------

EXEC NAME: statemate
[1;32mTEST REPORT: SUCCESS.[0m
Real cycles: 4806184
Real instructions: 1288416
BOOT file: /home/mrabiai/Bureau/herd-ware/sw/embench-iot/hex/SIM/WAESP32AU1V210/statemate.boot8.hex
iROM file: /home/mrabiai/Bureau/herd-ware/sw/embench-iot/hex/SIM/WAESP32AU1V210/statemate.irom8.hex
Simulation fast clock cycles (/1): 9621358
Simulation main clock cycles (/2): 4810679

------------------------------
           HART: 0
------------------------------
Cycles: 4810674
Time: 4810674
Retired instructions: 1289869
ALU instructions: 904387
BRU instructions: 141670
MUL instructions: 0
DIV instructions: 0
Load instructions: 481666
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
32-bit instructions: 1289869
0 read port: 31472
1 read port: 621430
2 read port: 636967
Taken BR: 68854
Taken BR forward: 51092
Taken BR backward: 17762
Not taken BR: 37416
Not taken BR forward: 35440
Not taken BR backward: 1976
Mispredicted instructions: 85865
Mispredicted BR: 58977
Mispredicted BR taken: 53081
Mispredicted BR forward taken: 41270
Mispredicted BR backward taken: 11811
Mispredicted BR not taken: 5896
Mispredicted BR forward not taken: 3928
Mispredicted BR backward not taken: 1968
Mispredicted JALR: 11802
Mispredicted CALL: 11151
Mispredicted RET: 11802
Partial instructions: 0
Instruction buffer full: 0
Instruction buffer dead: 338
Wait source dependency: 119961
Wait MUL unit: 0
Wait DIV unit: 0
Wait data request: 548882
Wait data acknowledgement: 37342
Empty buffer for misaligned instructions: 0
Empty fetch port: 3079564
Empty commit port: 3520805
L1I hits: 1166486
L1I misses: 171670
L1I prefetches: 0
L1D hits: 862882
L1D misses: 5
L1D prefetches: 0
L2 hits: 1039131
L2 misses: 104206
L2 prefetches: 0
------------------------------

EXEC NAME: tarfind
[1;32mTEST REPORT: SUCCESS.[0m
Real cycles: 2180499
Real instructions: 1036979
BOOT file: /home/mrabiai/Bureau/herd-ware/sw/embench-iot/hex/SIM/WAESP32AU1V210/tarfind.boot8.hex
iROM file: /home/mrabiai/Bureau/herd-ware/sw/embench-iot/hex/SIM/WAESP32AU1V210/tarfind.irom8.hex
Simulation fast clock cycles (/1): 4484770
Simulation main clock cycles (/2): 2242385

------------------------------
           HART: 0
------------------------------
Cycles: 2242380
Time: 2242380
Retired instructions: 1063855
ALU instructions: 774788
BRU instructions: 193733
MUL instructions: 36960
DIV instructions: 36960
Load instructions: 80482
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
32-bit instructions: 1063855
0 read port: 154748
1 read port: 471480
2 read port: 437627
Taken BR: 89385
Taken BR forward: 12770
Taken BR backward: 76615
Not taken BR: 20511
Not taken BR forward: 15275
Not taken BR backward: 5236
Mispredicted instructions: 16347
Mispredicted BR: 11722
Mispredicted BR taken: 7598
Mispredicted BR forward taken: 1824
Mispredicted BR backward taken: 5774
Mispredicted BR not taken: 4124
Mispredicted BR forward not taken: 696
Mispredicted BR backward not taken: 3428
Mispredicted JALR: 4433
Mispredicted CALL: 1629
Mispredicted RET: 1312
Partial instructions: 0
Instruction buffer full: 0
Instruction buffer dead: 55941
Wait source dependency: 143259
Wait MUL unit: 36960
Wait DIV unit: 554250
Wait data request: 354052
Wait data acknowledgement: 78150
Empty buffer for misaligned instructions: 0
Empty fetch port: 79199
Empty commit port: 1178525
L1I hits: 1146626
L1I misses: 271
L1I prefetches: 0
L1D hits: 246858
L1D misses: 7736
L1D prefetches: 0
L2 hits: 264748
L2 misses: 7901
L2 prefetches: 0
------------------------------

EXEC NAME: ud
[1;32mTEST REPORT: SUCCESS.[0m
Real cycles: 6877627
Real instructions: 3358071
BOOT file: /home/mrabiai/Bureau/herd-ware/sw/embench-iot/hex/SIM/WAESP32AU1V210/ud.boot8.hex
iROM file: /home/mrabiai/Bureau/herd-ware/sw/embench-iot/hex/SIM/WAESP32AU1V210/ud.irom8.hex
Simulation fast clock cycles (/1): 13771952
Simulation main clock cycles (/2): 6885976

------------------------------
           HART: 0
------------------------------
Cycles: 6885971
Time: 6885971
Retired instructions: 3361436
ALU instructions: 2595107
BRU instructions: 597715
MUL instructions: 128673
DIV instructions: 31059
Load instructions: 448238
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
32-bit instructions: 3361436
0 read port: 130187
1 read port: 1822524
2 read port: 1408725
Taken BR: 281146
Taken BR forward: 97617
Taken BR backward: 183529
Not taken BR: 199697
Not taken BR forward: 103558
Not taken BR backward: 96139
Mispredicted instructions: 258848
Mispredicted BR: 215933
Mispredicted BR taken: 158248
Mispredicted BR forward taken: 70240
Mispredicted BR backward taken: 88008
Mispredicted BR not taken: 57685
Mispredicted BR forward not taken: 8878
Mispredicted BR backward not taken: 48807
Mispredicted JALR: 16285
Mispredicted CALL: 13322
Mispredicted RET: 16285
Partial instructions: 0
Instruction buffer full: 0
Instruction buffer dead: 67
Wait source dependency: 411277
Wait MUL unit: 128673
Wait DIV unit: 124236
Wait data request: 17876
Wait data acknowledgement: 89
Empty buffer for misaligned instructions: 0
Empty fetch port: 2674334
Empty commit port: 3524535
L1I hits: 3850601
L1I misses: 156825
L1I prefetches: 0
L1D hits: 649803
L1D misses: 28
L1D prefetches: 0
L2 hits: 673838
L2 misses: 143787
L2 prefetches: 0
------------------------------

EXEC NAME: wikisort
[1;32mTEST REPORT: SUCCESS.[0m
Real cycles: 4018486
Real instructions: 1256853
BOOT file: /home/mrabiai/Bureau/herd-ware/sw/embench-iot/hex/SIM/WAESP32AU1V210/wikisort.boot8.hex
iROM file: /home/mrabiai/Bureau/herd-ware/sw/embench-iot/hex/SIM/WAESP32AU1V210/wikisort.irom8.hex
Simulation fast clock cycles (/1): 16112258
Simulation main clock cycles (/2): 8056129

------------------------------
           HART: 0
------------------------------
Cycles: 8056124
Time: 8056124
Retired instructions: 2523263
ALU instructions: 2018995
BRU instructions: 422350
MUL instructions: 58400
DIV instructions: 19308
Load instructions: 390743
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
32-bit instructions: 2523263
0 read port: 97577
1 read port: 1466971
2 read port: 958715
Taken BR: 145187
Taken BR forward: 84889
Taken BR backward: 60298
Not taken BR: 120113
Not taken BR forward: 107793
Not taken BR backward: 12320
Mispredicted instructions: 171581
Mispredicted BR: 112735
Mispredicted BR taken: 101700
Mispredicted BR forward taken: 75564
Mispredicted BR backward taken: 26136
Mispredicted BR not taken: 11035
Mispredicted BR forward not taken: 7851
Mispredicted BR backward not taken: 3184
Mispredicted JALR: 24593
Mispredicted CALL: 21410
Mispredicted RET: 21842
Partial instructions: 0
Instruction buffer full: 0
Instruction buffer dead: 31629
Wait source dependency: 225898
Wait MUL unit: 58400
Wait DIV unit: 543632
Wait data request: 242181
Wait data acknowledgement: 120350
Empty buffer for misaligned instructions: 0
Empty fetch port: 4347636
Empty commit port: 5532861
L1I hits: 2727142
L1I misses: 263738
L1I prefetches: 0
L1D hits: 597825
L1D misses: 11359
L1D prefetches: 0
L2 hits: 1046171
L2 misses: 258398
L2 prefetches: 0
------------------------------


"""


extract_cache_stats(report_data)