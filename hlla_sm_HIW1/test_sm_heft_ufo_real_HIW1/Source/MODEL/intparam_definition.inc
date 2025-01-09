ccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc
c      written by the UFO converter
ccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc

C     Parameters that should not be recomputed event by event.
C     
      IF(READLHA) THEN

        G = 2 * DSQRT(AS*PI)  ! for the first init

        MDL_MZ__EXP__2 = MDL_MZ**2

        MDL_MZ__EXP__4 = MDL_MZ**4

        MDL_SQRT__2 = SQRT(DCMPLX(2.000000D+00))

        MDL_MH__EXP__8 = MDL_MH**8

        MDL_MT__EXP__8 = MDL_MT**8

        MDL_MH__EXP__6 = MDL_MH**6

        MDL_MT__EXP__6 = MDL_MT**6

        MDL_MH__EXP__4 = MDL_MH**4

        MDL_MT__EXP__4 = MDL_MT**4

        MDL_MH__EXP__2 = MDL_MH**2

        MDL_MT__EXP__2 = MDL_MT**2

        MDL_MZ__EXP__6 = MDL_MZ**6

        MDL_MZ__EXP__8 = MDL_MZ**8

        MDL_COMPLEXI = DCMPLX(0.000000D+00,1.000000D+00)

        MDL_AEW = 1.000000D+00/AEWM1

        MDL_MW = SQRT(DCMPLX(MDL_MZ__EXP__2/2.000000D+00
     $   +SQRT(DCMPLX(MDL_MZ__EXP__4/4.000000D+00-(MDL_AEW*PI
     $   *MDL_MZ__EXP__2)/(MDL_GF*MDL_SQRT__2)))))

        MDL_SQRT__AEW = SQRT(DCMPLX(MDL_AEW))

        MDL_EE = 2.000000D+00*MDL_SQRT__AEW*SQRT(DCMPLX(PI))

        MDL_MW__EXP__2 = MDL_MW**2

        MDL_SW2 = 1.000000D+00-MDL_MW__EXP__2/MDL_MZ__EXP__2

        MDL_CW = SQRT(DCMPLX(1.000000D+00-MDL_SW2))

        MDL_SQRT__SW2 = SQRT(DCMPLX(MDL_SW2))

        MDL_SW = MDL_SQRT__SW2

        MDL_G1 = MDL_EE/MDL_CW

        MDL_GW = MDL_EE/MDL_SW

        MDL_VEV = (2.000000D+00*MDL_MW*MDL_SW)/MDL_EE

        MDL_MW__EXP__8 = MDL_MW**8

        MDL_MW__EXP__6 = MDL_MW**6

        MDL_MW__EXP__4 = MDL_MW**4

        MDL_KHYY = (MDL_AEW*(7.071303D+00+(4.000000D+00*(-1.333333D+00
     $   -(8.000000D+00*MDL_MH__EXP__8)/(5.197500D+04*MDL_MT__EXP__8)
     $   -(1.300000D+01*MDL_MH__EXP__6)/(1.260000D+04*MDL_MT__EXP__6)
     $   -MDL_MH__EXP__4/(1.260000D+02*MDL_MT__EXP__4)-(7.000000D+00
     $   *MDL_MH__EXP__2)/(9.000000D+01*MDL_MT__EXP__2)))/3.000000D+00
     $   +(4.100000D+01*MDL_MH__EXP__8)/(3.465000D+04*MDL_MW__EXP__8)
     $   +(2.900000D+01*MDL_MH__EXP__6)/(4.200000D+03*MDL_MW__EXP__6)
     $   +(1.900000D+01*MDL_MH__EXP__4)/(4.200000D+02*MDL_MW__EXP__4)
     $   +(1.100000D+01*MDL_MH__EXP__2)/(3.000000D+01*MDL_MW__EXP__2)))
     $   /(2.000000D+00*PI*MDL_VEV)

        MDL_KHZY = (MDL_AEW*(-1.201021D+01-(4.000000D+00*(-3.333333D
     $   -01-(2.000000D+00*MDL_MH__EXP__8)/(5.197500D+04
     $   *MDL_MT__EXP__8)-(1.100000D+01*MDL_MZ__EXP__2)/(3.600000D+02
     $   *MDL_MT__EXP__2)-(1.100000D+01*MDL_MZ__EXP__4)/(2.520000D+03
     $   *MDL_MT__EXP__4)-(3.700000D+01*MDL_MZ__EXP__6)/(5.040000D+04
     $   *MDL_MT__EXP__6)-MDL_MZ__EXP__8/(7.425000D+03*MDL_MT__EXP__8)
     $   -(MDL_MH__EXP__6*(1.650794D-02+(2.080000D+02*MDL_MZ__EXP__2)
     $   /(5.197500D+04*MDL_MT__EXP__2)))/(6.400000D+01*MDL_MT__EXP__6)
     $   -(MDL_MH__EXP__4*(3.174603D-02+MDL_MZ__EXP__2/(1.500000D+02
     $   *MDL_MT__EXP__2)+(8.000000D+00*MDL_MZ__EXP__4)/(5.775000D+03
     $   *MDL_MT__EXP__4)))/(1.600000D+01*MDL_MT__EXP__4)
     $   -(MDL_MH__EXP__2*(7.777778D-02+(4.000000D+00*MDL_MZ__EXP__2)
     $   /(3.150000D+02*MDL_MT__EXP__2)+(2.900000D+01*MDL_MZ__EXP__4)
     $   /(1.260000D+04*MDL_MT__EXP__4)+(2.300000D+01*MDL_MZ__EXP__6)
     $   /(5.197500D+04*MDL_MT__EXP__6)))/(4.000000D+00*MDL_MT__EXP__2)
     $   )*(5.000000D-01-(4.000000D+00*MDL_SW2)/3.000000D+00))/(MDL_CW
     $   *MDL_SW)))/(2.000000D+00*PI*MDL_VEV)

        MDL_VEV__EXP__2 = MDL_VEV**2

        MDL_LAM = MDL_MH__EXP__2/(2.000000D+00*MDL_VEV__EXP__2)

        MDL_YB = (MDL_YMB*MDL_SQRT__2)/MDL_VEV

        MDL_YC = (MDL_YMC*MDL_SQRT__2)/MDL_VEV

        MDL_YDO = (MDL_YMDO*MDL_SQRT__2)/MDL_VEV

        MDL_YE = (MDL_YME*MDL_SQRT__2)/MDL_VEV

        MDL_YM = (MDL_YMM*MDL_SQRT__2)/MDL_VEV

        MDL_YS = (MDL_YMS*MDL_SQRT__2)/MDL_VEV

        MDL_YT = (MDL_YMT*MDL_SQRT__2)/MDL_VEV

        MDL_YTAU = (MDL_YMTAU*MDL_SQRT__2)/MDL_VEV

        MDL_YUP = (MDL_YMUP*MDL_SQRT__2)/MDL_VEV

        MDL_MUH = SQRT(DCMPLX(MDL_LAM*MDL_VEV__EXP__2))

        MDL_EE__EXP__2 = MDL_EE**2

        MDL_SW__EXP__2 = MDL_SW**2

        MDL_CW__EXP__2 = MDL_CW**2

      ENDIF
C     
C     Parameters that should be recomputed at an event by even basis.
C     
      AS = G**2/4/PI

      MDL_SQRT__AS = SQRT(DCMPLX(AS))

      MDL_G__EXP__2 = G**2

      MDL_KHGG = -(AS*(-1.236177D+00-(8.000000D+00*MDL_MH__EXP__8)
     $ /(5.197500D+04*MDL_MT__EXP__8)-(1.300000D+01*MDL_MH__EXP__6)
     $ /(1.260000D+04*MDL_MT__EXP__6)-MDL_MH__EXP__4/(1.260000D+02
     $ *MDL_MT__EXP__4)-(7.000000D+00*MDL_MH__EXP__2)/(9.000000D+01
     $ *MDL_MT__EXP__2)))/(4.000000D+00*PI*MDL_VEV)

C     
C     Definition of the EW coupling used in the write out of aqed
C     
      GAL(1) = 3.5449077018110318D0 / DSQRT(AEWM1)
      GAL(2) = 1D0

