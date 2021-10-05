# This script generates the opcode.h header file.

import functools
import sys
import tokenize

header = """
/* Auto-generated by Tools/scripts/generate_opcode_h.py from Lib/opcode.py */
#ifndef Py_OPCODE_H
#define Py_OPCODE_H
#ifdef __cplusplus
extern "C" {
#endif


    /* Instruction opcodes for compiled code */
#define PY_OPCODES(X)""".lstrip()

footer = """

#define OP(op, value) static const int op = value;
PY_OPCODES(OP)
#undef OP

/* EXCEPT_HANDLER is a special, implicit block type which is created when
   entering an except handler. It is not an opcode but we define it here
   as we want it to be available to both frameobject.c and ceval.c, while
   remaining private.*/
#define EXCEPT_HANDLER 257


enum cmp_op {PyCmp_LT=Py_LT, PyCmp_LE=Py_LE, PyCmp_EQ=Py_EQ, PyCmp_NE=Py_NE,
                PyCmp_GT=Py_GT, PyCmp_GE=Py_GE, PyCmp_IN, PyCmp_NOT_IN,
                PyCmp_IS, PyCmp_IS_NOT, PyCmp_EXC_MATCH, PyCmp_BAD};

#define HAS_ARG(op) ((op) >= HAVE_ARGUMENT)

#ifdef __cplusplus
}
#endif
#endif /* !Py_OPCODE_H */
"""


def main(opcode_py, outfile='Include/opcode.h'):
    opcode = {}
    if hasattr(tokenize, 'open'):
        fp = tokenize.open(opcode_py)   # Python 3.2+
    else:
        fp = open(opcode_py)            # Python 2.7
    with fp:
        code = fp.read()
    exec(code, opcode)
    opmap = opcode['opmap']

    max_op_len = functools.reduce(
        lambda m, elem: max(m, len(elem)), opcode['opname'], 0
    ) + 3 # 3-digit opcode length

    def write_line(opname, opnum):
        padding = max_op_len - len(opname)
        fobj.write(" \\\n  X(%s, %*d)" % (opname, padding, opnum))

    with open(outfile, 'w') as fobj:
        fobj.write(header)
        for name in opcode['opname']:
            if name in opmap:
                write_line(name, opmap[name])
            if name == 'POP_EXCEPT': # Special entry for HAVE_ARGUMENT
                write_line('HAVE_ARGUMENT', opcode['HAVE_ARGUMENT'])
        fobj.write(footer)

    print("%s regenerated from %s" % (outfile, opcode_py))


if __name__ == '__main__':
    main(sys.argv[1], sys.argv[2])
