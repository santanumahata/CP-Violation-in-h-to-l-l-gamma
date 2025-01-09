ccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc
c      written by the UFO converter
ccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc

      SUBROUTINE COUP1()

      IMPLICIT NONE
      INCLUDE 'model_functions.inc'

      DOUBLE PRECISION PI, ZERO
      PARAMETER  (PI=3.141592653589793D0)
      PARAMETER  (ZERO=0D0)
      INCLUDE 'input.inc'
      INCLUDE 'coupl.inc'
      GC_5910 = (MDL_EE*MDL_COMPLEXI)/(2.000000D+00*MDL_CTH*MDL_STH)
      GC_6173 = (MDL_EE*MDL_COMPLEXI*MDL_PROPCORR)/(2.000000D+00
     $ *MDL_CTH*MDL_STH)
      GC_6187 = -((MDL_EE*MDL_COMPLEXI*MDL_STH)/MDL_CTH)
      GC_6308 = -((MDL_EE*MDL_COMPLEXI*MDL_PROPCORR*MDL_STH)/MDL_CTH)
      GC_6361 = (2.000000D+00*MDL_COMPLEXI*MDL_GHZA)/MDL_VEVHAT
      GC_6379 = (2.000000D+00*MDL_COMPLEXI*MDL_GHZA*MDL_PROPCORR)
     $ /MDL_VEVHAT
      END
