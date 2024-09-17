import re

def extract_cpi(report):

    exec_blocks = re.findall(r"EXEC NAME: (.+?)\n.*?Real instructions: (\d+)", report, re.DOTALL)

    for exec_name,  instructions in exec_blocks:

        instructions = int(instructions)


      


        print(f"{exec_name}: instr number = {instructions}")


report_data = """

EXEC NAME: aha-mont64
[1;32mTEST REPORT: SUCCESS.[0m
Real cycles: 5594580
Real instructions: 4531262
BOOT file: /home/mrabiai/Bureau/herd-ware/sw/embench-iot/hex/SIM/WAESP32AU1V210Set4Data4/aha-mont64.boot8.hex
iROM file: /home/mrabiai/Bureau/herd-ware/sw/embench-iot/hex/SIM/WAESP32AU1V210Set4Data4/aha-mont64.irom8.hex
Simulation fast clock cycles (/1): 11218090
Simulation main clock cycles (/2): 5609045

------------------------------
           HART: 0
------------------------------
Cycles: 5609040
Time: 5609040
Retired instructions: 4542231
ALU instructions: 4040578
BRU instructions: 466013
MUL instructions: 35632
DIV instructions: 0
Load instructions: 9383
Store instructions: 3042
BR instructions: 460050
BR forward instructions: 257800
BR backward instructions: 202250
JAL instructions: 4679
JALR instructions: 1284
CALL instructions: 1284
RET instructions: 1284
Read cycle instructions: 2
Cache flush instructions: 0
16-bit instructions: 0
32-bit instructions: 4542231
0 read port: 4702
1 read port: 2410168
2 read port: 2127361
Taken BR: 354464
Taken BR forward: 167057
Taken BR backward: 187407
Not taken BR: 105586
Not taken BR forward: 90743
Not taken BR backward: 14843
Mispredicted instructions: 155024
Mispredicted BR: 150755
Mispredicted BR taken: 108978
Mispredicted BR forward taken: 73250
Mispredicted BR backward taken: 35728
Mispredicted BR not taken: 41777
Mispredicted BR forward not taken: 34249
Mispredicted BR backward not taken: 7528
Mispredicted JALR: 862
Mispredicted CALL: 1284
Mispredicted RET: 862
Partial instructions: 0
Instruction buffer full: 0
Instruction buffer dead: 1
Wait source dependency: 16560
Wait MUL unit: 71264
Wait DIV unit: 0
Wait data request: 1351
Wait data acknowledgement: 5658
Empty buffer for misaligned instructions: 0
Empty fetch port: 695183
Empty commit port: 1066809
L1I hits: 4971633
L1I misses: 28887
L1I prefetches: 0
L1D hits: 12403
L1D misses: 7
L1D prefetches: 0
L2 hits: 94785
L2 misses: 23388
L2 prefetches: 0
------------------------------

EXEC NAME: crc32
[1;31mTEST REPORT: FAILED.[0m
Real cycles: 6410008
Real instructions: 3831161
BOOT file: /home/mrabiai/Bureau/herd-ware/sw/embench-iot/hex/SIM/WAESP32AU1V210Set4Data4/crc32.boot8.hex
iROM file: /home/mrabiai/Bureau/herd-ware/sw/embench-iot/hex/SIM/WAESP32AU1V210Set4Data4/crc32.irom8.hex
Simulation fast clock cycles (/1): 12896708
Simulation main clock cycles (/2): 6448354

------------------------------
           HART: 0
------------------------------
Cycles: 6448349
Time: 6448349
Retired instructions: 3853897
ALU instructions: 3152923
BRU instructions: 525862
MUL instructions: 175104
DIV instructions: 0
Load instructions: 350231
Store instructions: 175315
BR instructions: 175285
BR forward instructions: 8
BR backward instructions: 175277
JAL instructions: 175290
JALR instructions: 175287
CALL instructions: 175287
RET instructions: 175287
Read cycle instructions: 2
Cache flush instructions: 0
16-bit instructions: 0
32-bit instructions: 3853897
0 read port: 525519
1 read port: 2102228
2 read port: 1226150
Taken BR: 175104
Taken BR forward: 1
Taken BR backward: 175103
Not taken BR: 181
Not taken BR forward: 7
Not taken BR backward: 174
Mispredicted instructions: 96324
Mispredicted BR: 96295
Mispredicted BR taken: 96123
Mispredicted BR forward taken: 1
Mispredicted BR backward taken: 96122
Mispredicted BR not taken: 172
Mispredicted BR forward not taken: 0
Mispredicted BR backward not taken: 172
Mispredicted JALR: 12
Mispredicted CALL: 14
Mispredicted RET: 12
Partial instructions: 0
Instruction buffer full: 0
Instruction buffer dead: 95892
Wait source dependency: 1858655
Wait MUL unit: 349866
Wait DIV unit: 0
Wait data request: 54
Wait data acknowledgement: 1158312
Empty buffer for misaligned instructions: 0
Empty fetch port: 289120
Empty commit port: 2594452
L1I hits: 4142833
L1I misses: 37
L1I prefetches: 0
L1D hits: 429634
L1D misses: 95897
L1D prefetches: 0
L2 hits: 553154
L2 misses: 5882
L2 prefetches: 0
------------------------------

EXEC NAME: cubic
[1;31mTEST REPORT: FAILED.[0m
Real cycles: 25801691
Real instructions: 7126176
BOOT file: /home/mrabiai/Bureau/herd-ware/sw/embench-iot/hex/SIM/WAESP32AU1V210Set4Data4/cubic.boot8.hex
iROM file: /home/mrabiai/Bureau/herd-ware/sw/embench-iot/hex/SIM/WAESP32AU1V210Set4Data4/cubic.irom8.hex
Simulation fast clock cycles (/1): 56769538
Simulation main clock cycles (/2): 28384769

------------------------------
           HART: 0
------------------------------
Cycles: 28384764
Time: 28384764
Retired instructions: 7839402
ALU instructions: 6465078
BRU instructions: 970627
MUL instructions: 372328
DIV instructions: 26114
Load instructions: 688760
Store instructions: 632225
BR instructions: 802519
BR forward instructions: 641967
BR backward instructions: 160552
JAL instructions: 120201
JALR instructions: 47907
CALL instructions: 47609
RET instructions: 47609
Read cycle instructions: 2
Cache flush instructions: 0
16-bit instructions: 0
32-bit instructions: 7839402
0 read port: 341060
1 read port: 3540685
2 read port: 3957657
Taken BR: 406557
Taken BR forward: 305476
Taken BR backward: 101081
Not taken BR: 395962
Not taken BR forward: 336491
Not taken BR backward: 59471
Mispredicted instructions: 556146
Mispredicted BR: 401346
Mispredicted BR taken: 344326
Mispredicted BR forward taken: 282238
Mispredicted BR backward taken: 62088
Mispredicted BR not taken: 57020
Mispredicted BR forward not taken: 36262
Mispredicted BR backward not taken: 20758
Mispredicted JALR: 47272
Mispredicted CALL: 47609
Mispredicted RET: 46974
Partial instructions: 0
Instruction buffer full: 0
Instruction buffer dead: 26542
Wait source dependency: 1008323
Wait MUL unit: 399476
Wait DIV unit: 577520
Wait data request: 184664
Wait data acknowledgement: 851872
Empty buffer for misaligned instructions: 0
Empty fetch port: 18023403
Empty commit port: 20545362
L1I hits: 8110862
L1I misses: 1144253
L1I prefetches: 0
L1D hits: 1299343
L1D misses: 16008
L1D prefetches: 0
L2 hits: 4181682
L2 misses: 962680
L2 prefetches: 0
------------------------------

EXEC NAME: edn
[1;31mTEST REPORT: FAILED.[0m
Real cycles: 6419746
Real instructions: 3920202
BOOT file: /home/mrabiai/Bureau/herd-ware/sw/embench-iot/hex/SIM/WAESP32AU1V210Set4Data4/edn.boot8.hex
iROM file: /home/mrabiai/Bureau/herd-ware/sw/embench-iot/hex/SIM/WAESP32AU1V210Set4Data4/edn.irom8.hex
Simulation fast clock cycles (/1): 12996620
Simulation main clock cycles (/2): 6498310

------------------------------
           HART: 0
------------------------------
Cycles: 6498305
Time: 6498305
Retired instructions: 3966671
ALU instructions: 2264456
BRU instructions: 360205
MUL instructions: 580008
DIV instructions: 0
Load instructions: 1331860
Store instructions: 111105
BR instructions: 359381
BR forward instructions: 187
BR backward instructions: 359194
JAL instructions: 459
JALR instructions: 365
CALL instructions: 365
RET instructions: 365
Read cycle instructions: 2
Cache flush instructions: 0
16-bit instructions: 0
32-bit instructions: 3966671
0 read port: 569
1 read port: 2246864
2 read port: 1719238
Taken BR: 348102
Taken BR forward: 90
Taken BR backward: 348012
Not taken BR: 11279
Not taken BR forward: 97
Not taken BR backward: 11182
Mispredicted instructions: 24143
Mispredicted BR: 23319
Mispredicted BR taken: 12122
Mispredicted BR forward taken: 90
Mispredicted BR backward taken: 12032
Mispredicted BR not taken: 11197
Mispredicted BR forward not taken: 19
Mispredicted BR backward not taken: 11178
Mispredicted JALR: 365
Mispredicted CALL: 365
Mispredicted RET: 365
Partial instructions: 0
Instruction buffer full: 0
Instruction buffer dead: 15774
Wait source dependency: 2036019
Wait MUL unit: 1025376
Wait DIV unit: 0
Wait data request: 109063
Wait data acknowledgement: 774084
Empty buffer for misaligned instructions: 0
Empty fetch port: 249430
Empty commit port: 2531634
L1I hits: 3607822
L1I misses: 18923
L1I prefetches: 0
L1D hits: 998339
L1D misses: 18816
L1D prefetches: 0
L2 hits: 243322
L2 misses: 14955
L2 prefetches: 0
------------------------------

EXEC NAME: huffbench
[1;32mTEST REPORT: SUCCESS.[0m
Real cycles: 4581092
Real instructions: 2598468
BOOT file: /home/mrabiai/Bureau/herd-ware/sw/embench-iot/hex/SIM/WAESP32AU1V210Set4Data4/huffbench.boot8.hex
iROM file: /home/mrabiai/Bureau/herd-ware/sw/embench-iot/hex/SIM/WAESP32AU1V210Set4Data4/huffbench.irom8.hex
Simulation fast clock cycles (/1): 10029822
Simulation main clock cycles (/2): 5014911

------------------------------
           HART: 0
------------------------------
Cycles: 5014906
Time: 5014906
Retired instructions: 2840277
ALU instructions: 2080856
BRU instructions: 598001
MUL instructions: 0
DIV instructions: 0
Load instructions: 665991
Store instructions: 200954
BR instructions: 545278
BR forward instructions: 270071
BR backward instructions: 275207
JAL instructions: 51449
JALR instructions: 1274
CALL instructions: 1261
RET instructions: 1261
Read cycle instructions: 2
Cache flush instructions: 0
16-bit instructions: 0
32-bit instructions: 2840277
0 read port: 54331
1 read port: 1792529
2 read port: 993417
Taken BR: 310595
Taken BR forward: 60364
Taken BR backward: 250231
Not taken BR: 234683
Not taken BR forward: 209707
Not taken BR backward: 24976
Mispredicted instructions: 166615
Mispredicted BR: 166116
Mispredicted BR taken: 125776
Mispredicted BR forward taken: 44324
Mispredicted BR backward taken: 81452
Mispredicted BR not taken: 40340
Mispredicted BR forward not taken: 25944
Mispredicted BR backward not taken: 14396
Mispredicted JALR: 146
Mispredicted CALL: 169
Mispredicted RET: 133
Partial instructions: 0
Instruction buffer full: 0
Instruction buffer dead: 10156
Wait source dependency: 1548244
Wait MUL unit: 0
Wait DIV unit: 0
Wait data request: 80810
Wait data acknowledgement: 607380
Empty buffer for misaligned instructions: 0
Empty fetch port: 362393
Empty commit port: 2174629
L1I hits: 3181877
L1I misses: 1207
L1I prefetches: 0
L1D hits: 694483
L1D misses: 7669
L1D prefetches: 0
L2 hits: 240565
L2 misses: 5656
L2 prefetches: 0
------------------------------

EXEC NAME: matmult-int
[1;32mTEST REPORT: SUCCESS.[0m
Real cycles: 8999781
Real instructions: 3183124
BOOT file: /home/mrabiai/Bureau/herd-ware/sw/embench-iot/hex/SIM/WAESP32AU1V210Set4Data4/matmult-int.boot8.hex
iROM file: /home/mrabiai/Bureau/herd-ware/sw/embench-iot/hex/SIM/WAESP32AU1V210Set4Data4/matmult-int.irom8.hex
Simulation fast clock cycles (/1): 18483252
Simulation main clock cycles (/2): 9241626

------------------------------
           HART: 0
------------------------------
Cycles: 9241621
Time: 9241621
Retired instructions: 3266799
ALU instructions: 2482427
BRU instructions: 407564
MUL instructions: 376000
DIV instructions: 800
Load instructions: 790836
Store instructions: 435654
BR instructions: 407440
BR forward instructions: 411
BR backward instructions: 407029
JAL instructions: 64
JALR instructions: 60
CALL instructions: 60
RET instructions: 60
Read cycle instructions: 2
Cache flush instructions: 0
16-bit instructions: 0
32-bit instructions: 3266799
0 read port: 104
1 read port: 1667291
2 read port: 1599404
Taken BR: 387105
Taken BR forward: 3
Taken BR backward: 387102
Not taken BR: 20335
Not taken BR forward: 408
Not taken BR backward: 19927
Mispredicted instructions: 40992
Mispredicted BR: 40959
Mispredicted BR taken: 21033
Mispredicted BR forward taken: 3
Mispredicted BR backward taken: 21030
Mispredicted BR not taken: 19926
Mispredicted BR forward not taken: 2
Mispredicted BR backward not taken: 19924
Mispredicted JALR: 14
Mispredicted CALL: 15
Mispredicted RET: 14
Partial instructions: 0
Instruction buffer full: 0
Instruction buffer dead: 352805
Wait source dependency: 5728280
Wait MUL unit: 752000
Wait DIV unit: 15145
Wait data request: 161921
Wait data acknowledgement: 3903501
Empty buffer for misaligned instructions: 0
Empty fetch port: 93767
Empty commit port: 5974822
L1I hits: 3741416
L1I misses: 77
L1I prefetches: 0
L1D hits: 849447
L1D misses: 376779
L1D prefetches: 0
L2 hits: 1874139
L2 misses: 64218
L2 prefetches: 0
------------------------------

EXEC NAME: md5sum
[1;32mTEST REPORT: SUCCESS.[0m
Real cycles: 2644993
Real instructions: 2046782
BOOT file: /home/mrabiai/Bureau/herd-ware/sw/embench-iot/hex/SIM/WAESP32AU1V210Set4Data4/md5sum.boot8.hex
iROM file: /home/mrabiai/Bureau/herd-ware/sw/embench-iot/hex/SIM/WAESP32AU1V210Set4Data4/md5sum.irom8.hex
Simulation fast clock cycles (/1): 5410920
Simulation main clock cycles (/2): 2705460

------------------------------
           HART: 0
------------------------------
Cycles: 2705455
Time: 2705455
Retired instructions: 2089515
ALU instructions: 1814376
BRU instructions: 275079
MUL instructions: 52
DIV instructions: 0
Load instructions: 181996
Store instructions: 89277
BR instructions: 234179
BR forward instructions: 121643
BR backward instructions: 112536
JAL instructions: 40419
JALR instructions: 481
CALL instructions: 428
RET instructions: 428
Read cycle instructions: 2
Cache flush instructions: 0
16-bit instructions: 0
32-bit instructions: 2089515
0 read port: 41491
1 read port: 921341
2 read port: 1126683
Taken BR: 128030
Taken BR forward: 28394
Taken BR backward: 99636
Not taken BR: 106149
Not taken BR forward: 93249
Not taken BR backward: 12900
Mispredicted instructions: 30972
Mispredicted BR: 29852
Mispredicted BR taken: 27770
Mispredicted BR forward taken: 11026
Mispredicted BR backward taken: 16744
Mispredicted BR not taken: 2082
Mispredicted BR forward not taken: 1716
Mispredicted BR backward not taken: 366
Mispredicted JALR: 481
Mispredicted CALL: 428
Mispredicted RET: 428
Partial instructions: 0
Instruction buffer full: 0
Instruction buffer dead: 20288
Wait source dependency: 285552
Wait MUL unit: 104
Wait DIV unit: 0
Wait data request: 130648
Wait data acknowledgement: 386325
Empty buffer for misaligned instructions: 0
Empty fetch port: 121575
Empty commit port: 615940
L1I hits: 2196555
L1I misses: 2920
L1I prefetches: 0
L1D hits: 250128
L1D misses: 18104
L1D prefetches: 0
L2 hits: 170672
L2 misses: 10238
L2 prefetches: 0
------------------------------

EXEC NAME: minver
[1;31mTEST REPORT: FAILED.[0m
Real cycles: 20562470
Real instructions: 4964001
BOOT file: /home/mrabiai/Bureau/herd-ware/sw/embench-iot/hex/SIM/WAESP32AU1V210Set4Data4/minver.boot8.hex
iROM file: /home/mrabiai/Bureau/herd-ware/sw/embench-iot/hex/SIM/WAESP32AU1V210Set4Data4/minver.irom8.hex
Simulation fast clock cycles (/1): 41203572
Simulation main clock cycles (/2): 20601786

------------------------------
           HART: 0
------------------------------
Cycles: 20601781
Time: 20601781
Retired instructions: 4973404
ALU instructions: 3934154
BRU instructions: 928041
MUL instructions: 73392
DIV instructions: 35584
Load instructions: 422641
Store instructions: 385418
BR instructions: 722283
BR forward instructions: 638869
BR backward instructions: 83414
JAL instructions: 137910
JALR instructions: 67848
CALL instructions: 67292
RET instructions: 67292
Read cycle instructions: 2
Cache flush instructions: 0
16-bit instructions: 0
32-bit instructions: 4973404
0 read port: 296963
1 read port: 2761932
2 read port: 1914509
Taken BR: 321947
Taken BR forward: 279129
Taken BR backward: 42818
Not taken BR: 400336
Not taken BR forward: 359740
Not taken BR backward: 40596
Mispredicted instructions: 530200
Mispredicted BR: 333152
Mispredicted BR taken: 313739
Mispredicted BR forward taken: 273700
Mispredicted BR backward taken: 40039
Mispredicted BR not taken: 19413
Mispredicted BR forward not taken: 9590
Mispredicted BR backward not taken: 9823
Mispredicted JALR: 64697
Mispredicted CALL: 66181
Mispredicted RET: 64141
Partial instructions: 0
Instruction buffer full: 0
Instruction buffer dead: 31701
Wait source dependency: 437032
Wait MUL unit: 58936
Wait DIV unit: 845120
Wait data request: 34199
Wait data acknowledgement: 397475
Empty buffer for misaligned instructions: 0
Empty fetch port: 13501210
Empty commit port: 15628377
L1I hits: 5429330
L1I misses: 949047
L1I prefetches: 0
L1D hits: 802461
L1D misses: 3354
L1D prefetches: 0
L2 hits: 3492680
L2 misses: 656362
L2 prefetches: 0
------------------------------

EXEC NAME: nbody
[1;32mTEST REPORT: SUCCESS.[0m
Real cycles: 12125741
Real instructions: 3475621
BOOT file: /home/mrabiai/Bureau/herd-ware/sw/embench-iot/hex/SIM/WAESP32AU1V210Set4Data4/nbody.boot8.hex
iROM file: /home/mrabiai/Bureau/herd-ware/sw/embench-iot/hex/SIM/WAESP32AU1V210Set4Data4/nbody.irom8.hex
Simulation fast clock cycles (/1): 48538550
Simulation main clock cycles (/2): 24269275

------------------------------
           HART: 0
------------------------------
Cycles: 24269270
Time: 24269270
Retired instructions: 6955184
ALU instructions: 5595361
BRU instructions: 1107241
MUL instructions: 232756
DIV instructions: 16216
Load instructions: 347587
Store instructions: 277435
BR instructions: 938673
BR forward instructions: 712883
BR backward instructions: 225790
JAL instructions: 118386
JALR instructions: 50182
CALL instructions: 50178
RET instructions: 50178
Read cycle instructions: 2
Cache flush instructions: 0
16-bit instructions: 0
32-bit instructions: 6955184
0 read port: 291512
1 read port: 3386957
2 read port: 3276715
Taken BR: 450164
Taken BR forward: 300844
Taken BR backward: 149320
Not taken BR: 488509
Not taken BR forward: 412039
Not taken BR backward: 76470
Mispredicted instructions: 583439
Mispredicted BR: 417047
Mispredicted BR taken: 340383
Mispredicted BR forward taken: 269696
Mispredicted BR backward taken: 70687
Mispredicted BR not taken: 76664
Mispredicted BR forward not taken: 56502
Mispredicted BR backward not taken: 20162
Mispredicted JALR: 49543
Mispredicted CALL: 49401
Mispredicted RET: 49539
Partial instructions: 0
Instruction buffer full: 0
Instruction buffer dead: 18095
Wait source dependency: 292062
Wait MUL unit: 441512
Wait DIV unit: 464206
Wait data request: 66451
Wait data acknowledgement: 294816
Empty buffer for misaligned instructions: 0
Empty fetch port: 15455382
Empty commit port: 17314086
L1I hits: 7434985
L1I misses: 1016743
L1I prefetches: 0
L1D hits: 616886
L1D misses: 4494
L1D prefetches: 0
L2 hits: 3467751
L2 misses: 852744
L2 prefetches: 0
------------------------------

EXEC NAME: nettle-aes
[1;32mTEST REPORT: SUCCESS.[0m
Real cycles: 14002413
Real instructions: 4431936
BOOT file: /home/mrabiai/Bureau/herd-ware/sw/embench-iot/hex/SIM/WAESP32AU1V210Set4Data4/nettle-aes.boot8.hex
iROM file: /home/mrabiai/Bureau/herd-ware/sw/embench-iot/hex/SIM/WAESP32AU1V210Set4Data4/nettle-aes.irom8.hex
Simulation fast clock cycles (/1): 28384632
Simulation main clock cycles (/2): 14192316

------------------------------
           HART: 0
------------------------------
Cycles: 14192311
Time: 14192311
Retired instructions: 4494625
ALU instructions: 4346598
BRU instructions: 78933
MUL instructions: 0
DIV instructions: 8216
Load instructions: 845412
Store instructions: 61824
BR instructions: 77878
BR forward instructions: 10522
BR backward instructions: 67356
JAL instructions: 647
JALR instructions: 408
CALL instructions: 407
RET instructions: 407
Read cycle instructions: 2
Cache flush instructions: 0
16-bit instructions: 0
32-bit instructions: 4494625
0 read port: 2087
1 read port: 3080687
2 read port: 1411851
Taken BR: 48867
Taken BR forward: 239
Taken BR backward: 48628
Not taken BR: 29011
Not taken BR forward: 10283
Not taken BR backward: 18728
Mispredicted instructions: 25126
Mispredicted BR: 24150
Mispredicted BR taken: 15404
Mispredicted BR forward taken: 239
Mispredicted BR backward taken: 15165
Mispredicted BR not taken: 8746
Mispredicted BR forward not taken: 871
Mispredicted BR backward not taken: 7875
Mispredicted JALR: 329
Mispredicted CALL: 407
Mispredicted RET: 328
Partial instructions: 0
Instruction buffer full: 0
Instruction buffer dead: 505964
Wait source dependency: 114390
Wait MUL unit: 0
Wait DIV unit: 44240
Wait data request: 1101822
Wait data acknowledgement: 8286533
Empty buffer for misaligned instructions: 0
Empty fetch port: 1803858
Empty commit port: 9697686
L1I hits: 4927820
L1I misses: 107849
L1I prefetches: 0
L1D hits: 322928
L1D misses: 557591
L1D prefetches: 0
L2 hits: 2138670
L2 misses: 579375
L2 prefetches: 0
------------------------------

EXEC NAME: nettle-sha256
[1;32mTEST REPORT: SUCCESS.[0m
Real cycles: 11894113
Real instructions: 4016186
BOOT file: /home/mrabiai/Bureau/herd-ware/sw/embench-iot/hex/SIM/WAESP32AU1V210Set4Data4/nettle-sha256.boot8.hex
iROM file: /home/mrabiai/Bureau/herd-ware/sw/embench-iot/hex/SIM/WAESP32AU1V210Set4Data4/nettle-sha256.irom8.hex
Simulation fast clock cycles (/1): 23843704
Simulation main clock cycles (/2): 11921852

------------------------------
           HART: 0
------------------------------
Cycles: 11921847
Time: 11921847
Retired instructions: 4025353
ALU instructions: 3922898
BRU instructions: 48167
MUL instructions: 0
DIV instructions: 0
Load instructions: 423338
Store instructions: 155415
BR instructions: 38619
BR forward instructions: 8583
BR backward instructions: 30036
JAL instructions: 5727
JALR instructions: 3821
CALL instructions: 3344
RET instructions: 3344
Read cycle instructions: 2
Cache flush instructions: 0
16-bit instructions: 0
32-bit instructions: 4025353
0 read port: 8122
1 read port: 1791560
2 read port: 2225671
Taken BR: 27175
Taken BR forward: 3333
Taken BR backward: 23842
Not taken BR: 11444
Not taken BR forward: 5250
Not taken BR backward: 6194
Mispredicted instructions: 24649
Mispredicted BR: 15101
Mispredicted BR taken: 10332
Mispredicted BR forward taken: 3333
Mispredicted BR backward taken: 6999
Mispredicted BR not taken: 4769
Mispredicted BR forward not taken: 956
Mispredicted BR backward not taken: 3813
Mispredicted JALR: 3821
Mispredicted CALL: 3344
Mispredicted RET: 3344
Partial instructions: 0
Instruction buffer full: 0
Instruction buffer dead: 8139
Wait source dependency: 164342
Wait MUL unit: 0
Wait DIV unit: 0
Wait data request: 99302
Wait data acknowledgement: 540026
Empty buffer for misaligned instructions: 0
Empty fetch port: 7440658
Empty commit port: 7896494
L1I hits: 3583105
L1I misses: 485583
L1I prefetches: 0
L1D hits: 543915
L1D misses: 10671
L1D prefetches: 0
L2 hits: 1635988
L2 misses: 479274
L2 prefetches: 0
------------------------------

EXEC NAME: nsichneu
[1;32mTEST REPORT: SUCCESS.[0m
Real cycles: 13248187
Real instructions: 2236758
BOOT file: /home/mrabiai/Bureau/herd-ware/sw/embench-iot/hex/SIM/WAESP32AU1V210Set4Data4/nsichneu.boot8.hex
iROM file: /home/mrabiai/Bureau/herd-ware/sw/embench-iot/hex/SIM/WAESP32AU1V210Set4Data4/nsichneu.irom8.hex
Simulation fast clock cycles (/1): 26520864
Simulation main clock cycles (/2): 13260432

------------------------------
           HART: 0
------------------------------
Cycles: 13260427
Time: 13260427
Retired instructions: 2238947
ALU instructions: 1232319
BRU instructions: 1006620
MUL instructions: 0
DIV instructions: 0
Load instructions: 1227119
Store instructions: 3759
BR instructions: 770048
BR forward instructions: 694867
BR backward instructions: 75181
JAL instructions: 236559
JALR instructions: 13
CALL instructions: 12
RET instructions: 12
Read cycle instructions: 2
Cache flush instructions: 0
16-bit instructions: 0
32-bit instructions: 2238947
0 read port: 236577
1 read port: 1228519
2 read port: 773851
Taken BR: 186047
Taken BR forward: 147843
Taken BR backward: 38204
Not taken BR: 584001
Not taken BR forward: 547024
Not taken BR backward: 36977
Mispredicted instructions: 444798
Mispredicted BR: 208226
Mispredicted BR taken: 186041
Mispredicted BR forward taken: 147843
Mispredicted BR backward taken: 38198
Mispredicted BR not taken: 22185
Mispredicted BR forward not taken: 17253
Mispredicted BR backward not taken: 4932
Mispredicted JALR: 13
Mispredicted CALL: 12
Mispredicted RET: 12
Partial instructions: 0
Instruction buffer full: 0
Instruction buffer dead: 3
Wait source dependency: 3655469
Wait MUL unit: 0
Wait DIV unit: 0
Wait data request: 42
Wait data acknowledgement: 798448
Empty buffer for misaligned instructions: 0
Empty fetch port: 6907589
Empty commit port: 11021480
L1I hits: 2677606
L1I misses: 491627
L1I prefetches: 0
L1D hits: 1230855
L1D misses: 7
L1D prefetches: 0
L2 hits: 1476188
L2 misses: 494089
L2 prefetches: 0
------------------------------

EXEC NAME: picojpeg
[1;31mTEST REPORT: FAILED.[0m
Real cycles: 8706820
Real instructions: 4140477
BOOT file: /home/mrabiai/Bureau/herd-ware/sw/embench-iot/hex/SIM/WAESP32AU1V210Set4Data4/picojpeg.boot8.hex
iROM file: /home/mrabiai/Bureau/herd-ware/sw/embench-iot/hex/SIM/WAESP32AU1V210Set4Data4/picojpeg.irom8.hex
Simulation fast clock cycles (/1): 20310826
Simulation main clock cycles (/2): 10155413

------------------------------
           HART: 0
------------------------------
Cycles: 10155408
Time: 10155408
Retired instructions: 4831694
ALU instructions: 3777271
BRU instructions: 478875
MUL instructions: 123116
DIV instructions: 0
Load instructions: 998817
Store instructions: 581925
BR instructions: 401444
BR forward instructions: 218735
BR backward instructions: 182709
JAL instructions: 51770
JALR instructions: 25661
CALL instructions: 24464
RET instructions: 24464
Read cycle instructions: 2
Cache flush instructions: 0
16-bit instructions: 0
32-bit instructions: 4831694
0 read port: 65911
1 read port: 3058120
2 read port: 1707663
Taken BR: 303869
Taken BR forward: 140121
Taken BR backward: 163748
Not taken BR: 97575
Not taken BR forward: 78614
Not taken BR backward: 18961
Mispredicted instructions: 159954
Mispredicted BR: 109359
Mispredicted BR taken: 92032
Mispredicted BR forward taken: 65950
Mispredicted BR backward taken: 26082
Mispredicted BR not taken: 17327
Mispredicted BR forward not taken: 14256
Mispredicted BR backward not taken: 3071
Mispredicted JALR: 13966
Mispredicted CALL: 19215
Mispredicted RET: 12769
Partial instructions: 0
Instruction buffer full: 0
Instruction buffer dead: 22932
Wait source dependency: 1111515
Wait MUL unit: 238406
Wait DIV unit: 0
Wait data request: 244372
Wait data acknowledgement: 1284788
Empty buffer for misaligned instructions: 0
Empty fetch port: 3634254
Empty commit port: 5323714
L1I hits: 4665787
L1I misses: 250717
L1I prefetches: 0
L1D hits: 1182034
L1D misses: 43986
L1D prefetches: 0
L2 hits: 1554831
L2 misses: 184759
L2 prefetches: 0
------------------------------

EXEC NAME: primecount
[1;32mTEST REPORT: SUCCESS.[0m
Real cycles: 4929158
Real instructions: 2148524
BOOT file: /home/mrabiai/Bureau/herd-ware/sw/embench-iot/hex/SIM/WAESP32AU1V210Set4Data4/primecount.boot8.hex
iROM file: /home/mrabiai/Bureau/herd-ware/sw/embench-iot/hex/SIM/WAESP32AU1V210Set4Data4/primecount.irom8.hex
Simulation fast clock cycles (/1): 19718104
Simulation main clock cycles (/2): 9859052

------------------------------
           HART: 0
------------------------------
Cycles: 9859047
Time: 9859047
Retired instructions: 4297207
ALU instructions: 2339336
BRU instructions: 1826347
MUL instructions: 131516
DIV instructions: 0
Load instructions: 751215
Store instructions: 119748
BR instructions: 1760420
BR forward instructions: 1261752
BR backward instructions: 498668
JAL instructions: 65913
JALR instructions: 14
CALL instructions: 14
RET instructions: 14
Read cycle instructions: 2
Cache flush instructions: 0
16-bit instructions: 0
32-bit instructions: 4297207
0 read port: 65932
1 read port: 2099925
2 read port: 2131350
Taken BR: 704496
Taken BR forward: 325379
Taken BR backward: 379117
Not taken BR: 1055924
Not taken BR forward: 936373
Not taken BR backward: 119551
Mispredicted instructions: 369059
Mispredicted BR: 369026
Mispredicted BR taken: 299389
Mispredicted BR forward taken: 173565
Mispredicted BR backward taken: 125824
Mispredicted BR not taken: 69637
Mispredicted BR forward not taken: 69633
Mispredicted BR backward not taken: 4
Mispredicted JALR: 14
Mispredicted CALL: 14
Mispredicted RET: 14
Partial instructions: 0
Instruction buffer full: 0
Instruction buffer dead: 0
Wait source dependency: 4091798
Wait MUL unit: 263032
Wait DIV unit: 0
Wait data request: 23
Wait data acknowledgement: 751258
Empty buffer for misaligned instructions: 0
Empty fetch port: 738740
Empty commit port: 5561840
L1I hits: 5404337
L1I misses: 44
L1I prefetches: 0
L1D hits: 870935
L1D misses: 13
L1D prefetches: 0
L2 hits: 119910
L2 misses: 50
L2 prefetches: 0
------------------------------

EXEC NAME: qrduino
[1;31mTEST REPORT: FAILED.[0m
Real cycles: 4832336
Real instructions: 3144736
BOOT file: /home/mrabiai/Bureau/herd-ware/sw/embench-iot/hex/SIM/WAESP32AU1V210Set4Data4/qrduino.boot8.hex
iROM file: /home/mrabiai/Bureau/herd-ware/sw/embench-iot/hex/SIM/WAESP32AU1V210Set4Data4/qrduino.irom8.hex
Simulation fast clock cycles (/1): 11618050
Simulation main clock cycles (/2): 5809025

------------------------------
           HART: 0
------------------------------
Cycles: 5809020
Time: 5809020
Retired instructions: 3778239
ALU instructions: 2745349
BRU instructions: 498725
MUL instructions: 94200
DIV instructions: 0
Load instructions: 1031114
Store instructions: 83434
BR instructions: 468008
BR forward instructions: 214062
BR backward instructions: 253946
JAL instructions: 27973
JALR instructions: 2744
CALL instructions: 2665
RET instructions: 2665
Read cycle instructions: 2
Cache flush instructions: 0
16-bit instructions: 0
32-bit instructions: 3778239
0 read port: 31316
1 read port: 2355848
2 read port: 1391075
Taken BR: 257878
Taken BR forward: 85166
Taken BR backward: 172712
Not taken BR: 210130
Not taken BR forward: 128896
Not taken BR backward: 81234
Mispredicted instructions: 166944
Mispredicted BR: 163622
Mispredicted BR taken: 123735
Mispredicted BR forward taken: 45670
Mispredicted BR backward taken: 78065
Mispredicted BR not taken: 39887
Mispredicted BR forward not taken: 18295
Mispredicted BR backward not taken: 21592
Mispredicted JALR: 816
Mispredicted CALL: 734
Mispredicted RET: 737
Partial instructions: 0
Instruction buffer full: 0
Instruction buffer dead: 1056
Wait source dependency: 1435980
Wait MUL unit: 182544
Wait DIV unit: 0
Wait data request: 10997
Wait data acknowledgement: 507976
Empty buffer for misaligned instructions: 0
Empty fetch port: 412380
Empty commit port: 2030781
L1I hits: 3845185
L1I misses: 5414
L1I prefetches: 0
L1D hits: 685818
L1D misses: 877
L1D prefetches: 0
L2 hits: 103530
L2 misses: 5436
L2 prefetches: 0
------------------------------

EXEC NAME: sglib-combined
[1;32mTEST REPORT: SUCCESS.[0m
Real cycles: 6128278
Real instructions: 2622218
BOOT file: /home/mrabiai/Bureau/herd-ware/sw/embench-iot/hex/SIM/WAESP32AU1V210Set4Data4/sglib-combined.boot8.hex
iROM file: /home/mrabiai/Bureau/herd-ware/sw/embench-iot/hex/SIM/WAESP32AU1V210Set4Data4/sglib-combined.irom8.hex
Simulation fast clock cycles (/1): 12734866
Simulation main clock cycles (/2): 6367433

------------------------------
           HART: 0
------------------------------
Cycles: 6367428
Time: 6367428
Retired instructions: 2720386
ALU instructions: 1941417
BRU instructions: 681421
MUL instructions: 0
DIV instructions: 9100
Load instructions: 734387
Store instructions: 322590
BR instructions: 549478
BR forward instructions: 307281
BR backward instructions: 242197
JAL instructions: 93888
JALR instructions: 38055
CALL instructions: 38054
RET instructions: 38054
Read cycle instructions: 2
Cache flush instructions: 0
16-bit instructions: 0
32-bit instructions: 2720386
0 read port: 121074
1 read port: 1517561
2 read port: 1081751
Taken BR: 223815
Taken BR forward: 95145
Taken BR backward: 128670
Not taken BR: 325663
Not taken BR forward: 212136
Not taken BR backward: 113527
Mispredicted instructions: 193207
Mispredicted BR: 162615
Mispredicted BR taken: 123077
Mispredicted BR forward taken: 60025
Mispredicted BR backward taken: 63052
Mispredicted BR not taken: 39538
Mispredicted BR forward not taken: 17796
Mispredicted BR backward not taken: 21742
Mispredicted JALR: 9990
Mispredicted CALL: 11744
Mispredicted RET: 9989
Partial instructions: 0
Instruction buffer full: 0
Instruction buffer dead: 62709
Wait source dependency: 2419594
Wait MUL unit: 0
Wait DIV unit: 52594
Wait data request: 134532
Wait data acknowledgement: 1331895
Empty buffer for misaligned instructions: 0
Empty fetch port: 794726
Empty commit port: 3647042
L1I hits: 3213569
L1I misses: 35202
L1I prefetches: 0
L1D hits: 910741
L1D misses: 65814
L1D prefetches: 0
L2 hits: 676672
L2 misses: 48537
L2 prefetches: 0
------------------------------

EXEC NAME: slre
[1;32mTEST REPORT: SUCCESS.[0m
Real cycles: 8346896
Real instructions: 2590544
BOOT file: /home/mrabiai/Bureau/herd-ware/sw/embench-iot/hex/SIM/WAESP32AU1V210Set4Data4/slre.boot8.hex
iROM file: /home/mrabiai/Bureau/herd-ware/sw/embench-iot/hex/SIM/WAESP32AU1V210Set4Data4/slre.irom8.hex
Simulation fast clock cycles (/1): 16848122
Simulation main clock cycles (/2): 8424061

------------------------------
           HART: 0
------------------------------
Cycles: 8424056
Time: 8424056
Retired instructions: 2614381
ALU instructions: 1826109
BRU instructions: 665498
MUL instructions: 0
DIV instructions: 0
Load instructions: 590566
Store instructions: 297430
BR instructions: 534601
BR forward instructions: 440463
BR backward instructions: 94138
JAL instructions: 98028
JALR instructions: 32869
CALL instructions: 32868
RET instructions: 32868
Read cycle instructions: 2
Cache flush instructions: 0
16-bit instructions: 0
32-bit instructions: 2614381
0 read port: 119800
1 read port: 1406215
2 read port: 1088366
Taken BR: 180270
Taken BR forward: 131980
Taken BR backward: 48290
Not taken BR: 354331
Not taken BR forward: 308483
Not taken BR backward: 45848
Mispredicted instructions: 267273
Mispredicted BR: 163792
Mispredicted BR taken: 147055
Mispredicted BR forward taken: 112255
Mispredicted BR backward taken: 34800
Mispredicted BR not taken: 16737
Mispredicted BR forward not taken: 15787
Mispredicted BR backward not taken: 950
Mispredicted JALR: 29761
Mispredicted CALL: 25764
Mispredicted RET: 29760
Partial instructions: 0
Instruction buffer full: 0
Instruction buffer dead: 3258
Wait source dependency: 843995
Wait MUL unit: 0
Wait DIV unit: 0
Wait data request: 195782
Wait data acknowledgement: 578715
Empty buffer for misaligned instructions: 0
Empty fetch port: 4371408
Empty commit port: 5809675
L1I hits: 2937557
L1I misses: 303406
L1I prefetches: 0
L1D hits: 757642
L1D misses: 7458
L1D prefetches: 0
L2 hits: 1331184
L2 misses: 188584
L2 prefetches: 0
------------------------------

EXEC NAME: st
[1;31mTEST REPORT: FAILED.[0m
Real cycles: 16436534
Real instructions: 3931418
BOOT file: /home/mrabiai/Bureau/herd-ware/sw/embench-iot/hex/SIM/WAESP32AU1V210Set4Data4/st.boot8.hex
iROM file: /home/mrabiai/Bureau/herd-ware/sw/embench-iot/hex/SIM/WAESP32AU1V210Set4Data4/st.irom8.hex
Simulation fast clock cycles (/1): 35410102
Simulation main clock cycles (/2): 17705051

------------------------------
           HART: 0
------------------------------
Cycles: 17705046
Time: 17705046
Retired instructions: 4235169
ALU instructions: 3470242
BRU instructions: 582498
MUL instructions: 146664
DIV instructions: 25760
Load instructions: 242049
Store instructions: 204052
BR instructions: 444339
BR forward instructions: 416210
BR backward instructions: 28129
JAL instructions: 94169
JALR instructions: 43990
CALL instructions: 43989
RET instructions: 43989
Read cycle instructions: 2
Cache flush instructions: 0
16-bit instructions: 0
32-bit instructions: 4235169
0 read port: 228792
1 read port: 2088227
2 read port: 1918150
Taken BR: 191348
Taken BR forward: 177844
Taken BR backward: 13504
Not taken BR: 252991
Not taken BR forward: 238366
Not taken BR backward: 14625
Mispredicted instructions: 343385
Mispredicted BR: 208922
Mispredicted BR taken: 186890
Mispredicted BR forward taken: 174801
Mispredicted BR backward taken: 12089
Mispredicted BR not taken: 22032
Mispredicted BR forward not taken: 19404
Mispredicted BR backward not taken: 2628
Mispredicted JALR: 43089
Mispredicted CALL: 42063
Mispredicted RET: 43088
Partial instructions: 0
Instruction buffer full: 0
Instruction buffer dead: 27231
Wait source dependency: 284611
Wait MUL unit: 224784
Wait DIV unit: 723576
Wait data request: 35930
Wait data acknowledgement: 185287
Empty buffer for misaligned instructions: 0
Empty fetch port: 11939145
Empty commit port: 13469877
L1I hits: 4313669
L1I misses: 794603
L1I prefetches: 0
L1D hits: 432573
L1D misses: 3420
L1D prefetches: 0
L2 hits: 2681714
L2 misses: 665257
L2 prefetches: 0
------------------------------

EXEC NAME: statemate
[1;32mTEST REPORT: SUCCESS.[0m
Real cycles: 5713295
Real instructions: 1288416
BOOT file: /home/mrabiai/Bureau/herd-ware/sw/embench-iot/hex/SIM/WAESP32AU1V210Set4Data4/statemate.boot8.hex
iROM file: /home/mrabiai/Bureau/herd-ware/sw/embench-iot/hex/SIM/WAESP32AU1V210Set4Data4/statemate.irom8.hex
Simulation fast clock cycles (/1): 11436370
Simulation main clock cycles (/2): 5718185

------------------------------
           HART: 0
------------------------------
Cycles: 5718180
Time: 5718180
Retired instructions: 1289867
ALU instructions: 941724
BRU instructions: 141669
MUL instructions: 0
DIV instructions: 0
Load instructions: 481665
Store instructions: 528693
BR instructions: 106270
BR forward instructions: 86532
BR backward instructions: 19738
JAL instructions: 19667
JALR instructions: 15732
CALL instructions: 15732
RET instructions: 15732
Read cycle instructions: 2
Cache flush instructions: 0
16-bit instructions: 0
32-bit instructions: 1289867
0 read port: 31472
1 read port: 621428
2 read port: 636967
Taken BR: 68854
Taken BR forward: 51092
Taken BR backward: 17762
Not taken BR: 37416
Not taken BR forward: 35440
Not taken BR backward: 1976
Mispredicted instructions: 103213
Mispredicted BR: 67815
Mispredicted BR taken: 63882
Mispredicted BR forward taken: 50110
Mispredicted BR backward taken: 13772
Mispredicted BR not taken: 3933
Mispredicted BR forward not taken: 1965
Mispredicted BR backward not taken: 1968
Mispredicted JALR: 15731
Mispredicted CALL: 15732
Mispredicted RET: 15731
Partial instructions: 0
Instruction buffer full: 0
Instruction buffer dead: 1972
Wait source dependency: 239148
Wait MUL unit: 0
Wait DIV unit: 0
Wait data request: 319086
Wait data acknowledgement: 544652
Empty buffer for misaligned instructions: 0
Empty fetch port: 3959691
Empty commit port: 4428313
L1I hits: 1197375
L1I misses: 219804
L1I prefetches: 0
L1D hits: 862882
L1D misses: 5
L1D prefetches: 0
L2 hits: 1176340
L2 misses: 147265
L2 prefetches: 0
------------------------------

EXEC NAME: tarfind
[1;32mTEST REPORT: SUCCESS.[0m
Real cycles: 2302955
Real instructions: 1036980
BOOT file: /home/mrabiai/Bureau/herd-ware/sw/embench-iot/hex/SIM/WAESP32AU1V210Set4Data4/tarfind.boot8.hex
iROM file: /home/mrabiai/Bureau/herd-ware/sw/embench-iot/hex/SIM/WAESP32AU1V210Set4Data4/tarfind.irom8.hex
Simulation fast clock cycles (/1): 4734808
Simulation main clock cycles (/2): 2367404

------------------------------
           HART: 0
------------------------------
Cycles: 2367399
Time: 2367399
Retired instructions: 1063854
ALU instructions: 774788
BRU instructions: 193732
MUL instructions: 36960
DIV instructions: 36960
Load instructions: 80482
Store instructions: 206835
BR instructions: 109896
BR forward instructions: 28045
BR backward instructions: 81851
JAL instructions: 40383
JALR instructions: 43453
CALL instructions: 40332
RET instructions: 40332
Read cycle instructions: 2
Cache flush instructions: 0
16-bit instructions: 0
32-bit instructions: 1063854
0 read port: 154748
1 read port: 471479
2 read port: 437627
Taken BR: 89385
Taken BR forward: 12770
Taken BR backward: 76615
Not taken BR: 20511
Not taken BR forward: 15275
Not taken BR backward: 5236
Mispredicted instructions: 27219
Mispredicted BR: 23303
Mispredicted BR taken: 19257
Mispredicted BR forward taken: 2109
Mispredicted BR backward taken: 17148
Mispredicted BR not taken: 4046
Mispredicted BR forward not taken: 623
Mispredicted BR backward not taken: 3423
Mispredicted JALR: 3565
Mispredicted CALL: 1788
Mispredicted RET: 444
Partial instructions: 0
Instruction buffer full: 0
Instruction buffer dead: 56486
Wait source dependency: 780019
Wait MUL unit: 73918
Wait DIV unit: 517290
Wait data request: 295638
Wait data acknowledgement: 438717
Empty buffer for misaligned instructions: 0
Empty fetch port: 132298
Empty commit port: 1303545
L1I hits: 1165688
L1I misses: 1269
L1I prefetches: 0
L1D hits: 246383
L1D misses: 8187
L1D prefetches: 0
L2 hits: 269555
L2 misses: 8898
L2 prefetches: 0
------------------------------

EXEC NAME: ud
[1;31mTEST REPORT: FAILED.[0m
Real cycles: 10798920
Real instructions: 3358071
BOOT file: /home/mrabiai/Bureau/herd-ware/sw/embench-iot/hex/SIM/WAESP32AU1V210Set4Data4/ud.boot8.hex
iROM file: /home/mrabiai/Bureau/herd-ware/sw/embench-iot/hex/SIM/WAESP32AU1V210Set4Data4/ud.irom8.hex
Simulation fast clock cycles (/1): 21619264
Simulation main clock cycles (/2): 10809632

------------------------------
           HART: 0
------------------------------
Cycles: 10809627
Time: 10809627
Retired instructions: 3361307
ALU instructions: 2595014
BRU instructions: 597677
MUL instructions: 128673
DIV instructions: 31059
Load instructions: 448203
Store instructions: 210536
BR instructions: 480804
BR forward instructions: 201154
BR backward instructions: 279650
JAL instructions: 79885
JALR instructions: 36988
CALL instructions: 36988
RET instructions: 36988
Read cycle instructions: 2
Cache flush instructions: 0
16-bit instructions: 0
32-bit instructions: 3361307
0 read port: 130189
1 read port: 1822430
2 read port: 1408688
Taken BR: 281124
Taken BR forward: 97615
Taken BR backward: 183509
Not taken BR: 199680
Not taken BR forward: 103539
Not taken BR backward: 96141
Mispredicted instructions: 371573
Mispredicted BR: 267022
Mispredicted BR taken: 195289
Mispredicted BR forward taken: 97615
Mispredicted BR backward taken: 97674
Mispredicted BR not taken: 71733
Mispredicted BR forward not taken: 23664
Mispredicted BR backward not taken: 48069
Mispredicted JALR: 36988
Mispredicted CALL: 30582
Mispredicted RET: 36988
Partial instructions: 0
Instruction buffer full: 0
Instruction buffer dead: 20768
Wait source dependency: 1047236
Wait MUL unit: 162690
Wait DIV unit: 461448
Wait data request: 38277
Wait data acknowledgement: 402210
Empty buffer for misaligned instructions: 0
Empty fetch port: 5339557
Empty commit port: 7448320
L1I hits: 4055891
L1I misses: 341717
L1I prefetches: 0
L1D hits: 637936
L1D misses: 11859
L1D prefetches: 0
L2 hits: 1323713
L2 misses: 277119
L2 prefetches: 0
------------------------------

EXEC NAME: wikisort
[1;31mTEST REPORT: FAILED.[0m
Real cycles: 4249281
Real instructions: 1266876
BOOT file: /home/mrabiai/Bureau/herd-ware/sw/embench-iot/hex/SIM/WAESP32AU1V210Set4Data4/wikisort.boot8.hex
iROM file: /home/mrabiai/Bureau/herd-ware/sw/embench-iot/hex/SIM/WAESP32AU1V210Set4Data4/wikisort.irom8.hex
Simulation fast clock cycles (/1): 17043344
Simulation main clock cycles (/2): 8521672

------------------------------
           HART: 0
------------------------------
Cycles: 8521667
Time: 8521667
Retired instructions: 2537727
ALU instructions: 2031383
BRU instructions: 424424
MUL instructions: 58400
DIV instructions: 19308
Load instructions: 390176
Store instructions: 224616
BR instructions: 267131
BR forward instructions: 195176
BR backward instructions: 71955
JAL instructions: 41193
JALR instructions: 116100
CALL instructions: 69151
RET instructions: 69151
Read cycle instructions: 2
Cache flush instructions: 0
16-bit instructions: 0
32-bit instructions: 2537727
0 read port: 97497
1 read port: 1473330
2 read port: 966900
Taken BR: 143410
Taken BR forward: 83741
Taken BR backward: 59669
Not taken BR: 123721
Not taken BR forward: 111435
Not taken BR backward: 12286
Mispredicted instructions: 169726
Mispredicted BR: 107864
Mispredicted BR taken: 96571
Mispredicted BR forward taken: 73866
Mispredicted BR backward taken: 22705
Mispredicted BR not taken: 11293
Mispredicted BR forward not taken: 8024
Mispredicted BR backward not taken: 3269
Mispredicted JALR: 25121
Mispredicted CALL: 23052
Mispredicted RET: 22357
Partial instructions: 0
Instruction buffer full: 0
Instruction buffer dead: 31648
Wait source dependency: 463726
Wait MUL unit: 39548
Wait DIV unit: 531956
Wait data request: 170985
Wait data acknowledgement: 468964
Empty buffer for misaligned instructions: 0
Empty fetch port: 4558991
Empty commit port: 5983940
L1I hits: 2710710
L1I misses: 280869
L1I prefetches: 0
L1D hits: 594655
L1D misses: 13855
L1D prefetches: 0
L2 hits: 1111407
L2 misses: 274446
L2 prefetches: 0
------------------------------



"""

extract_cpi(report_data)
