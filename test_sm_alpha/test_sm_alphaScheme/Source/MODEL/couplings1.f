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
      GC_6162 = (MDL_EE*MDL_COMPLEXI*MDL_PROPCORR)/(2.000000D+00
     $ *MDL_CTH*MDL_STH)
      GC_6294 = -((MDL_EE*MDL_COMPLEXI*MDL_PROPCORR*MDL_STH)/MDL_CTH)
      GC_6341 = -(MDL_EE*MDL_COMPLEXI)/(2.000000D+00*MDL_CTH*MDL_STH*(
     $ -1.000000D+00+2.000000D+00*MDL_STH__EXP__2))
      GC_6345 = (MDL_EE*MDL_COMPLEXI*MDL_STH)/(MDL_CTH*(-1.000000D+00
     $ +2.000000D+00*MDL_STH__EXP__2))
      GC_6348 = (-2.000000D+00*MDL_EE*MDL_COMPLEXI*MDL_STH__EXP__3)
     $ /(MDL_CTH*(-1.000000D+00+2.000000D+00*MDL_STH__EXP__2))
      GC_6365 = (2.000000D+00*MDL_COMPLEXI*MDL_GHZA)/MDL_VEVHAT
      GC_6383 = (2.000000D+00*MDL_COMPLEXI*MDL_GHZA*MDL_PROPCORR)
     $ /MDL_VEVHAT
      END
