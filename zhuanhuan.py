from sparkai.core.messages import ChatMessage


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
