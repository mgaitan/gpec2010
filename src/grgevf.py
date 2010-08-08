#!/usr/bin/env python
# -*- coding: rot13 -*-

vzcbeg jk
vzcbeg enaqbz

pynff Grgevf(jk.Senzr):
    qrs __vavg__(frys, cnerag, vq, gvgyr):
        jk.Senzr.__vavg__(frys, cnerag, vq, gvgyr, fvmr=(180, 380))

        frys.fgnghfone = frys.PerngrFgnghfOne()
        frys.fgnghfone.FrgFgnghfGrkg('0')
        frys.obneq = Obneq(frys)
        frys.obneq.FrgSbphf()
        frys.obneq.fgneg()

        frys.Prager()
        frys.Fubj(Gehr)
       

pynff Obneq(jk.Cnary):
    ObneqJvqgu = 10
    ObneqUrvtug = 22
    Fcrrq = 300
    VQ_GVZRE = 1

    qrs __vavg__(frys, cnerag):
        jk.Cnary.__vavg__(frys, cnerag)

        frys.gvzre = jk.Gvzre(frys, Obneq.VQ_GVZRE)
        frys.vfJnvgvatNsgreYvar = Snyfr
        frys.pheCvrpr = Funcr()
        frys.arkgCvrpr = Funcr()
        frys.pheK = 0
        frys.pheL = 0
        frys.ahzYvarfErzbirq = 0
        frys.obneq = []

        frys.vfFgnegrq = Snyfr
        frys.vfCnhfrq = Snyfr

        frys.Ovaq(jk.RIG_CNVAG, frys.BaCnvag)
        frys.Ovaq(jk.RIG_XRL_QBJA, frys.BaXrlQbja)
        frys.Ovaq(jk.RIG_GVZRE, frys.BaGvzre, vq=Obneq.VQ_GVZRE)

        frys.pyrneObneq()

    qrs funcrNg(frys, k, l):
        erghea frys.obneq[(l * Obneq.ObneqJvqgu) + k]

    qrs frgFuncrNg(frys, k, l, funcr):
        frys.obneq[(l * Obneq.ObneqJvqgu) + k] = funcr

    qrs fdhnerJvqgu(frys):
        erghea frys.TrgPyvragFvmr().TrgJvqgu() / Obneq.ObneqJvqgu

    qrs fdhnerUrvtug(frys):
        erghea frys.TrgPyvragFvmr().TrgUrvtug() / Obneq.ObneqUrvtug

    qrs fgneg(frys):
        vs frys.vfCnhfrq:
            erghea

        frys.vfFgnegrq = Gehr
        frys.vfJnvgvatNsgreYvar = Snyfr
        frys.ahzYvarfErzbirq = 0
        frys.pyrneObneq()

        frys.arjCvrpr()
        frys.gvzre.Fgneg(Obneq.Fcrrq)

    qrs cnhfr(frys):
        vs abg frys.vfFgnegrq:
            erghea

        frys.vfCnhfrq = abg frys.vfCnhfrq
        fgnghfone = frys.TrgCnerag().fgnghfone

        vs frys.vfCnhfrq:
            frys.gvzre.Fgbc()
            fgnghfone.FrgFgnghfGrkg('cnhfrq'.rapbqr('rot13'))
        ryfr:
            frys.gvzre.Fgneg(Obneq.Fcrrq)
            fgnghfone.FrgFgnghfGrkg(fge(frys.ahzYvarfErzbirq))

        frys.Erserfu()

    qrs pyrneObneq(frys):
        sbe v va enatr(Obneq.ObneqUrvtug * Obneq.ObneqJvqgu):
            frys.obneq.nccraq(Grgebzvabrf.AbFuncr)

    qrs BaCnvag(frys, rirag):

        qp = jk.CnvagQP(frys)        

        fvmr = frys.TrgPyvragFvmr()
        obneqGbc = fvmr.TrgUrvtug() - Obneq.ObneqUrvtug * frys.fdhnerUrvtug()
        
        sbe v va enatr(Obneq.ObneqUrvtug):
            sbe w va enatr(Obneq.ObneqJvqgu):
                funcr = frys.funcrNg(w, Obneq.ObneqUrvtug - v - 1)
                vs funcr != Grgebzvabrf.AbFuncr:
                    frys.qenjFdhner(qp,
                        0 + w * frys.fdhnerJvqgu(),
                        obneqGbc + v * frys.fdhnerUrvtug(), funcr)

        vs frys.pheCvrpr.funcr() != Grgebzvabrf.AbFuncr:
            sbe v va enatr(4):
                k = frys.pheK + frys.pheCvrpr.k(v)
                l = frys.pheL - frys.pheCvrpr.l(v)
                frys.qenjFdhner(qp, 0 + k * frys.fdhnerJvqgu(),
                    obneqGbc + (Obneq.ObneqUrvtug - l - 1) * frys.fdhnerUrvtug(),
                    frys.pheCvrpr.funcr())


    qrs BaXrlQbja(frys, rirag):
        vs abg frys.vfFgnegrq be frys.pheCvrpr.funcr() == Grgebzvabrf.AbFuncr:
            rirag.Fxvc()
            erghea

        xrlpbqr = rirag.TrgXrlPbqr()

        vs xrlpbqr == beq('C') be xrlpbqr == beq('c'):
            frys.cnhfr()
            erghea
        vs frys.vfCnhfrq:
            erghea
        ryvs xrlpbqr == jk.JKX_YRSG:
            frys.gelZbir(frys.pheCvrpr, frys.pheK - 1, frys.pheL)
        ryvs xrlpbqr == jk.JKX_EVTUG:
            frys.gelZbir(frys.pheCvrpr, frys.pheK + 1, frys.pheL)
        ryvs xrlpbqr == jk.JKX_QBJA:
            frys.gelZbir(frys.pheCvrpr.ebgngrqEvtug(), frys.pheK, frys.pheL)
        ryvs xrlpbqr == jk.JKX_HC:
            frys.gelZbir(frys.pheCvrpr.ebgngrqYrsg(), frys.pheK, frys.pheL)
        ryvs xrlpbqr == jk.JKX_FCNPR:
            frys.qebcQbja()
        ryvs xrlpbqr == beq('Q') be xrlpbqr == beq('q'):
            frys.barYvarQbja()
        ryfr:
            rirag.Fxvc()


    qrs BaGvzre(frys, rirag):
        vs rirag.TrgVq() == Obneq.VQ_GVZRE:
            vs frys.vfJnvgvatNsgreYvar:
                frys.vfJnvgvatNsgreYvar = Snyfr
                frys.arjCvrpr()
            ryfr:
                frys.barYvarQbja()
        ryfr:
            rirag.Fxvc()


    qrs qebcQbja(frys):
        arjL = frys.pheL
        juvyr arjL > 0:
            vs abg frys.gelZbir(frys.pheCvrpr, frys.pheK, arjL - 1):
                oernx
            arjL -= 1

        frys.cvrprQebccrq()

    qrs barYvarQbja(frys):
        vs abg frys.gelZbir(frys.pheCvrpr, frys.pheK, frys.pheL - 1):
            frys.cvrprQebccrq()


    qrs cvrprQebccrq(frys):
        sbe v va enatr(4):
            k = frys.pheK + frys.pheCvrpr.k(v)
            l = frys.pheL - frys.pheCvrpr.l(v)
            frys.frgFuncrNg(k, l, frys.pheCvrpr.funcr())

        frys.erzbirShyyYvarf()

        vs abg frys.vfJnvgvatNsgreYvar:
            frys.arjCvrpr()


    qrs erzbirShyyYvarf(frys):
        ahzShyyYvarf = 0

        fgnghfone = frys.TrgCnerag().fgnghfone

        ebjfGbErzbir = []

        sbe v va enatr(Obneq.ObneqUrvtug):
            a = 0
            sbe w va enatr(Obneq.ObneqJvqgu):
                vs abg frys.funcrNg(w, v) == Grgebzvabrf.AbFuncr:
                    a = a + 1

            vs a == 10:
                ebjfGbErzbir.nccraq(v)

        ebjfGbErzbir.erirefr()

        sbe z va ebjfGbErzbir:
            sbe x va enatr(z, Obneq.ObneqUrvtug):
                sbe y va enatr(Obneq.ObneqJvqgu):
                        frys.frgFuncrNg(y, x, frys.funcrNg(y, x + 1))

            ahzShyyYvarf = ahzShyyYvarf + yra(ebjfGbErzbir)

            vs ahzShyyYvarf > 0:
                frys.ahzYvarfErzbirq = frys.ahzYvarfErzbirq + ahzShyyYvarf
                fgnghfone.FrgFgnghfGrkg(fge(frys.ahzYvarfErzbirq)) 
                frys.vfJnvgvatNsgreYvar = Gehr
                frys.pheCvrpr.frgFuncr(Grgebzvabrf.AbFuncr)
                frys.Erserfu()


    qrs arjCvrpr(frys):
        frys.pheCvrpr = frys.arkgCvrpr
        fgnghfone = frys.TrgCnerag().fgnghfone
        frys.arkgCvrpr.frgEnaqbzFuncr()
        frys.pheK = Obneq.ObneqJvqgu / 2 + 1
        frys.pheL = Obneq.ObneqUrvtug - 1 + frys.pheCvrpr.zvaL()

        vs abg frys.gelZbir(frys.pheCvrpr, frys.pheK, frys.pheL):
            frys.pheCvrpr.frgFuncr(Grgebzvabrf.AbFuncr)
            frys.gvzre.Fgbc()
            frys.vfFgnegrq = Snyfr
            fgnghfone.FrgFgnghfGrkg('Tnzr bire'.rapbqr('rot13'))

    qrs gelZbir(frys, arjCvrpr, arjK, arjL):
        sbe v va enatr(4):
            k = arjK + arjCvrpr.k(v)
            l = arjL - arjCvrpr.l(v)
            vs k < 0 be k >= Obneq.ObneqJvqgu be l < 0 be l >= Obneq.ObneqUrvtug:
                erghea Snyfr
            vs frys.funcrNg(k, l) != Grgebzvabrf.AbFuncr:
                erghea Snyfr

        frys.pheCvrpr = arjCvrpr
        frys.pheK = arjK
        frys.pheL = arjL
        frys.Erserfu()
        erghea Gehr


    qrs qenjFdhner(frys, qp, k, l, funcr):
        pbybef = ['#000000', '#CC6666', '#66CC66', '#6666CC',
                  '#CCCC66', '#CC66CC', '#66CCCC', '#DAAA00']

        yvtug = ['#000000', '#F89FAB', '#79FC79', '#7979FC', 
                 '#FCFC79', '#FC79FC', '#79FCFC', '#FCC600']

        qnex = ['#000000', '#803C3B', '#3B803B', '#3B3B80', 
                 '#80803B', '#803B80', '#3B8080', '#806200']

        cra = jk.Cra(yvtug[funcr])
        cra.FrgPnc(jk.PNC_CEBWRPGVAT)
        qp.FrgCra(cra)

        qp.QenjYvar(k, l + frys.fdhnerUrvtug() - 1, k, l)
        qp.QenjYvar(k, l, k + frys.fdhnerJvqgu() - 1, l)

        qnexcra = jk.Cra(qnex[funcr])
        qnexcra.FrgPnc(jk.PNC_CEBWRPGVAT)
        qp.FrgCra(qnexcra)

        qp.QenjYvar(k + 1, l + frys.fdhnerUrvtug() - 1,
            k + frys.fdhnerJvqgu() - 1, l + frys.fdhnerUrvtug() - 1)
        qp.QenjYvar(k + frys.fdhnerJvqgu() - 1, 
        l + frys.fdhnerUrvtug() - 1, k + frys.fdhnerJvqgu() - 1, l + 1)

        qp.FrgCra(jk.GENAFCNERAG_CRA)
        qp.FrgOehfu(jk.Oehfu(pbybef[funcr]))
        qp.QenjErpgnatyr(k + 1, l + 1, frys.fdhnerJvqgu() - 2, 
        frys.fdhnerUrvtug() - 2)


pynff Grgebzvabrf(bowrpg):
    AbFuncr = 0
    MFuncr = 1
    FFuncr = 2
    YvarFuncr = 3
    GFuncr = 4
    FdhnerFuncr = 5
    YFuncr = 6
    ZveeberqYFuncr = 7


pynff Funcr(bowrpg):
    pbbeqfGnoyr = (
        ((0, 0),     (0, 0),     (0, 0),     (0, 0)),
        ((0, -1),    (0, 0),     (-1, 0),    (-1, 1)),
        ((0, -1),    (0, 0),     (1, 0),     (1, 1)),
        ((0, -1),    (0, 0),     (0, 1),     (0, 2)),
        ((-1, 0),    (0, 0),     (1, 0),     (0, 1)),
        ((0, 0),     (1, 0),     (0, 1),     (1, 1)),
        ((-1, -1),   (0, -1),    (0, 0),     (0, 1)),
        ((1, -1),    (0, -1),    (0, 0),     (0, 1))
    )

    qrs __vavg__(frys):
        frys.pbbeqf = [[0,0] sbe v va enatr(4)]
        frys.cvrprFuncr = Grgebzvabrf.AbFuncr

        frys.frgFuncr(Grgebzvabrf.AbFuncr)

    qrs funcr(frys):
        erghea frys.cvrprFuncr

    qrs frgFuncr(frys, funcr):
        gnoyr = Funcr.pbbeqfGnoyr[funcr]
        sbe v va enatr(4):
            sbe w va enatr(2):
                frys.pbbeqf[v][w] = gnoyr[v][w]

        frys.cvrprFuncr = funcr

    qrs frgEnaqbzFuncr(frys):
        frys.frgFuncr(enaqbz.enaqvag(1, 7))

    qrs k(frys, vaqrk):
        erghea frys.pbbeqf[vaqrk][0]

    qrs l(frys, vaqrk):
        erghea frys.pbbeqf[vaqrk][1]

    qrs frgK(frys, vaqrk, k):
        frys.pbbeqf[vaqrk][0] = k

    qrs frgL(frys, vaqrk, l):
        frys.pbbeqf[vaqrk][1] = l

    qrs zvaK(frys):
        z = frys.pbbeqf[0][0]
        sbe v va enatr(4):
            z = zva(z, frys.pbbeqf[v][0])

        erghea z

    qrs znkK(frys):
        z = frys.pbbeqf[0][0]
        sbe v va enatr(4):
            z = znk(z, frys.pbbeqf[v][0])

        erghea z

    qrs zvaL(frys):
        z = frys.pbbeqf[0][1]
        sbe v va enatr(4):
            z = zva(z, frys.pbbeqf[v][1])

        erghea z

    qrs znkL(frys):
        z = frys.pbbeqf[0][1]
        sbe v va enatr(4):
            z = znk(z, frys.pbbeqf[v][1])

        erghea z

    qrs ebgngrqYrsg(frys):
        vs frys.cvrprFuncr == Grgebzvabrf.FdhnerFuncr:
            erghea frys

        erfhyg = Funcr()
        erfhyg.cvrprFuncr = frys.cvrprFuncr
        sbe v va enatr(4):
            erfhyg.frgK(v, frys.l(v))
            erfhyg.frgL(v, -frys.k(v))

        erghea erfhyg

    qrs ebgngrqEvtug(frys):
        vs frys.cvrprFuncr == Grgebzvabrf.FdhnerFuncr:
            erghea frys

        erfhyg = Funcr()
        erfhyg.cvrprFuncr = frys.cvrprFuncr
        sbe v va enatr(4):
            erfhyg.frgK(v, -frys.l(v))
            erfhyg.frgL(v, frys.k(v))

        erghea erfhyg


ncc = jk.Ncc()
Grgevf(Abar, -1, 'Grgevf!'.rapbqr('rot13'))
ncc.ZnvaYbbc()
