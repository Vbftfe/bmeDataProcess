# 本文件提供函数用来找到ABP和PLETH信号在信号段中的位置
# 函数参数：recordPath: 需要读取的数据的路径(通过网络读取)
# 以字典形式返回，字典中有两个键，ＡＢＰ和ＰＬＥＴＨ，对应的值就是信号值组成的数组

import wfdb


def markSignal(recordPath):
    recordName = recordPath[11:len(recordPath)]
    pn_dir = f'published-projects/mimic3wdb/1.0/{recordPath[0:11]}'

    # record = wfdb.rdheader(recordName, pn_dir=pn_dir)
    # if 600*record.fs <= record.sig_len:
    record = wfdb.rdrecord(recordName, pn_dir=pn_dir)
    sig_names = record.sig_name
    res = {"ABP": 0, "PLETH": 0}
    ABP_idx = sig_names.index("ABP")
    PLETH_idx = sig_names.index("PLETH")
    res["ABP"] = record.p_signal[:, ABP_idx]
    res["PLETH"] = record.p_signal[:, PLETH_idx]
    # else:
    # res = None
    return res


# markSignal('31/3104269/3104269_0011')
