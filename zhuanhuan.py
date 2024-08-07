from sparkai.core.messages import ChatMessage

dict_to_g = {"user": "user", "system": "system", "assistant": "bot"}

dict_back_g = {"user": "user", "system": "system", "bot": "assistant"}


def w_to_t(w):
    tt = []
    for iw in w:
        tt.append(iw)
    return tt


def w_to_x(w):
    xx = []
    for iw in w:
        xx.append(ChatMessage(role=iw["role"], content=iw["content"]))
    return xx


def t_to_w(t):
    ww = []
    for it in t:
        ww.append(it)
    return ww


def t_to_x(t):
    xx = []
    for it in t:
        xx.append(ChatMessage(role=it["role"], content=it["content"]))
    return xx


def x_to_w(x):
    ww = []
    for ix in x:
        ww.append({"role": ix.role, "content": ix.content})
    return ww


def x_to_t(x):
    tt = []
    for ix in x:
        tt.append({"role": ix.role, "content": ix.content})
    return tt


def w_to_z(w):
    zz = []
    for iw in w:
        zz.append(iw)
    return zz


def x_to_z(x):
    zz = []
    for ix in x:
        zz.append({"role": ix.role, "content": ix.content})
    return zz


def z_to_w(z):
    ww = []
    for iz in z:
        ww.append(iz)
    return ww


def z_to_x(z):
    xx = []
    for iz in z:
        xx.append(ChatMessage(role=iz["role"], content=iz["content"]))
    return xx


def t_to_z(t):
    zz = []
    for it in t:
        zz.append(it)
    return zz


def z_to_t(z):
    tt = []
    for iz in z:
        tt.append(iz)
    return tt


def w_to_k(w):
    kk = []
    for iw in w:
        kk.append(iw)
    return kk


def x_to_k(x):
    kk = []
    for ix in x:
        kk.append({"role": ix.role, "content": ix.content})
    return kk


def k_to_w(k):
    ww = []
    for ik in k:
        ww.append(ik)
    return ww


def k_to_x(k):
    xx = []
    for ik in k:
        xx.append(ChatMessage(role=ik["role"], content=ik["content"]))
    return xx


def t_to_k(t):
    kk = []
    for it in t:
        kk.append(it)
    return kk


def k_to_t(k):
    tt = []
    for ik in k:
        tt.append(ik)
    return tt


def z_to_k(z):
    kk = []
    for iz in z:
        kk.append(iz)
    return kk


def k_to_z(k):
    zz = []
    for ik in k:
        zz.append(ik)
    return zz


def g_to_w(g):
    ww = []
    for ig in g:
        ww.append({"role": dict_back_g[ig["role"]], "content": ig["content"]})
    return ww


def g_to_x(g):
    xx = []
    for ig in g:
        xx.append(ChatMessage(role=dict_back_g[ig["role"]], content=ig["content"]))
    return xx


def g_to_t(g):
    tt = []
    for ig in g:
        tt.append({"role": dict_back_g[ig["role"]], "content": ig["content"]})
    return tt


def g_to_z(g):
    zz = []
    for ig in g:
        zz.append({"role": dict_back_g[ig["role"]], "content": ig["content"]})
    return zz


def g_to_k(g):
    kk = []
    for ig in g:
        kk.append({"role": dict_back_g[ig["role"]], "content": ig["content"]})
    return kk


def t_to_g(t):
    gg = []
    for it in t:
        gg.append({"role": dict_to_g[it["role"]], "content": it["content"]})
    return gg


def w_to_g(w):
    gg = []
    for iw in w:
        gg.append({"role": dict_to_g[iw["role"]], "content": iw["content"]})
    return gg


def x_to_g(x):
    gg = []
    for ix in x:
        gg.append({"role": dict_to_g[ix.role], "content": ix.content})
    return gg


def z_to_g(z):
    gg = []
    for iz in z:
        gg.append({"role": dict_to_g[iz["role"]], "content": iz["content"]})
    return gg


def k_to_g(k):
    gg = []
    for ik in k:
        gg.append({"role": dict_to_g[ik["role"]], "content": ik["content"]})
    return gg


def h_to_t(h):
    tt = []
    for ih in h:
        tt.append(ih)
    return tt


def h_to_w(h):
    ww = []
    for ih in h:
        ww.append(ih)
    return ww


def h_to_x(h):
    xx = []
    for ih in h:
        xx.append(ChatMessage(role=ih["role"], content=ih["content"]))
    return xx


def h_to_z(h):
    zz = []
    for ih in h:
        zz.append(ih)
    return zz


def h_to_k(h):
    kk = []
    for ih in h:
        kk.append({"role": dict_to_g[ih["role"]], "content": ih["content"]})
    return kk


def h_to_g(h):
    gg = []
    for ih in h:
        gg.append(ih)
    return gg


def t_to_h(t):
    hh = []
    for it in t:
        hh.append(it)
    return hh


def w_to_h(w):
    hh = []
    for iw in w:
        hh.append(iw)
    return hh


def x_to_h(x):
    hh = []
    for ix in x:
        hh.append({"role": ix.role, "content": ix.content})
    return hh


def z_to_h(z):
    hh = []
    for iz in z:
        hh.append(iz)
    return hh


def k_to_h(k):
    hh = []
    for ik in k:
        hh.append(ik)
    return hh


def g_to_h(g):
    hh = []
    for ig in g:
        hh.append({"role": dict_back_g[ig["role"]], "content": ig["content"]})
    return hh


def b_to_t(b):
    tt = []
    for ib in b:
        tt.append(ib)
    return tt


def b_to_w(b):
    ww = []
    for ib in b:
        ww.append(ib)
    return ww


def b_to_x(b):
    xx = []
    for ib in b:
        xx.append(ChatMessage(role=ib["role"], content=ib["content"]))
    return xx


def b_to_z(b):
    zz = []
    for ib in b:
        zz.append(ib)
    return zz


def b_to_k(b):
    kk = []
    for ib in b:
        kk.append({"role": dict_to_g[ib["role"]], "content": ib["content"]})
    return kk


def b_to_g(b):
    gg = []
    for ib in b:
        gg.append(ib)
    return gg


def t_to_b(t):
    bb = []
    for it in t:
        bb.append(it)
    return bb


def w_to_b(w):
    bb = []
    for iw in w:
        bb.append(iw)
    return bb


def x_to_b(x):
    bb = []
    for ix in x:
        bb.append({"role": ix.role, "content": ix.content})
    return bb


def z_to_b(z):
    bb = []
    for iz in z:
        bb.append(iz)
    return bb


def k_to_b(k):
    bb = []
    for ik in k:
        bb.append(ik)
    return bb


def g_to_b(g):
    bb = []
    for ig in g:
        bb.append(ig)
    return bb


def b_to_h(b):
    hh = []
    for ib in b:
        hh.append(ib)
    return hh


def h_to_b(h):
    bb = []
    for ih in h:
        bb.append(ih)
    return bb


def a_to_t(a):
    tt = []
    for ia in a:
        tt.append(ia)
    return tt


def a_to_h(a):
    hh = []
    for ia in a:
        hh.append(ia)
        hh = h_to_b(hh)


def a_to_b(a):
    bb = []
    for ia in a:
        bb.append(ia)
    return bb


def a_to_w(a):
    ww = []
    for ia in a:
        ww.append(ia)
    return ww


def a_to_x(a):
    xx = []
    for ia in a:
        xx.append(ChatMessage(role=ia["role"], content=ia["content"]))
    return xx


def a_to_z(a):
    zz = []
    for ia in a:
        zz.append(ia)
    return zz


def a_to_k(a):
    kk = []
    for ia in a:
        kk.append({"role": dict_to_g[ia["role"]], "content": ia["content"]})
    return kk


def a_to_g(a):
    gg = []
    for ia in a:
        gg.append(ia)
    return gg


def g_to_a(g):
    aa = []
    for ig in g:
        aa.append(ig)
    return aa


def t_to_a(t):
    aa = []
    for it in t:
        aa.append(it)
    return aa


def w_to_a(w):
    aa = []
    for iw in w:
        aa.append(iw)
    return aa


def x_to_a(x):
    aa = []
    for ix in x:
        aa.append({"role": ix.role, "content": ix.content})
    return aa


def z_to_a(z):
    aa = []
    for iz in z:
        aa.append(iz)
    return aa


def k_to_a(k):
    aa = []
    for ik in k:
        aa.append(ik)
    return aa


def b_to_a(b):
    aa = []
    for ib in b:
        aa.append(ib)
    return aa


def h_to_a(h):
    aa = []
    for ih in h:
        aa.append(ih)
    return aa
