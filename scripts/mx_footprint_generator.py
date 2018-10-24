import sys

def generate_footprint(size, isPCB, hasLED, isReversible):
    unit = f"{size:.2f}"
    mount = "PCB" if isPCB else "Plate"

    # header
    body = f'(module SW_Cherry_MX1A_{unit}u_{mount}{"_LED" if hasLED else ""}{"_Reversible" if isReversible else ""} (layer F.Cu) (tedit 5BB19F47)\n'
    body += f'  (descr "Cherry MX keyswitch, MX1A, {unit}u, {mount} mount, http://cherryamericas.com/wp-body/uploads/2014/12/mx_cat.pdf")\n'
    body += f'  (tags "cherry mx keyswitch MX1A {unit}u {mount}{" Reversible" if isReversible else ""}")\n'
    body += '  (fp_text reference REF** (at 0 -7.7) (layer F.SilkS)\n   (effects (font (size 1 1) (thickness 0.15)))\n  )\n  (fp_text value MX (at 0 7.874) (layer F.Fab) hide\n    (effects (font (size 1 1) (thickness 0.15)))\n  )\n'

    # cap size
    cap_size = 9.5 * size
    body += f'  (fp_line (start -{cap_size} -9.5) (end {cap_size} -9.5) (layer F.Fab) (width 0.1))\n' + \
              f'  (fp_line (start {cap_size} -9.5) (end {cap_size} 9.5) (layer F.Fab) (width 0.1))\n' + \
              f'  (fp_line (start {cap_size} 9.5) (end -{cap_size} 9.5) (layer F.Fab) (width 0.1))\n' + \
              f'  (fp_line (start -{cap_size} 9.5) (end -{cap_size} -9.5) (layer F.Fab) (width 0.1))\n'

    # plate hole
    body += '  (fp_line (start 7.8 -2.5) (end 7.8 -6) (layer Dwgs.User) (width 0.1))\n' + \
              '  (fp_line (start -7.8 6) (end -7.8 2.5) (layer Dwgs.User) (width 0.1))\n' + \
              '  (fp_line (start -7.8 2.5) (end -7 2.5) (layer Dwgs.User) (width 0.1))\n' + \
              '  (fp_line (start -7.8 6) (end -7 6) (layer Dwgs.User) (width 0.1))\n' + \
              '  (fp_line (start -7.8 -2.5) (end -7 -2.5) (layer Dwgs.User) (width 0.1))\n' + \
              '  (fp_line (start -7.8 -6) (end -7 -6) (layer Dwgs.User) (width 0.1))\n' + \
              '  (fp_line (start 7 -6) (end 7.8 -6) (layer Dwgs.User) (width 0.1))\n' + \
              '  (fp_line (start 7 -2.5) (end 7.8 -2.5) (layer Dwgs.User) (width 0.1))\n' + \
              '  (fp_line (start 7 6) (end 7.8 6) (layer Dwgs.User) (width 0.1))\n' + \
              '  (fp_line (start 7 2.5) (end 7.8 2.5) (layer Dwgs.User) (width 0.1))\n' + \
              '  (fp_line (start -7 -6) (end -7 -7) (layer Dwgs.User) (width 0.1))\n' + \
              '  (fp_line (start -7 7) (end -7 6) (layer Dwgs.User) (width 0.1))\n' + \
              '  (fp_line (start -7 -2.5) (end -7 2.5) (layer Dwgs.User) (width 0.1))\n' + \
              '  (fp_line (start -7 7) (end 7 7) (layer Dwgs.User) (width 0.1))\n' + \
              '  (fp_line (start 7 -2.5) (end 7 2.5) (layer Dwgs.User) (width 0.1))\n' + \
              '  (fp_line (start 7 7) (end 7 6) (layer Dwgs.User) (width 0.1))\n' + \
              '  (fp_line (start 7.8 6) (end 7.8 2.5) (layer Dwgs.User) (width 0.1))\n' + \
              '  (fp_line (start -7.8 -2.5) (end -7.8 -6) (layer Dwgs.User) (width 0.1))\n' + \
              '  (fp_line (start 7 -6) (end 7 -7) (layer Dwgs.User) (width 0.1))\n' + \
              '  (fp_line (start -7 -7) (end 7 -7) (layer Dwgs.User) (width 0.1))\n'

    # dimension
    body += '  (fp_line (start -7.8 -7.8) (end 7.8 -7.8) (layer Cmts.User) (width 0.15))\n' + \
              '  (fp_line (start 7.8 -7.8) (end 7.8 7.8) (layer Cmts.User) (width 0.15))\n' + \
              '  (fp_line (start 7.8 7.8) (end -7.8 7.8) (layer Cmts.User) (width 0.15))\n' + \
              '  (fp_line (start -7.8 7.8) (end -7.8 -7.8) (layer Cmts.User) (width 0.15))\n'

    # mounting holes
    if isPCB:
        body += '  (pad "" np_thru_hole circle (at 5.08 0) (size 1.7 1.7) (drill 1.7) (layers *.Cu *.Mask))\n' + \
                  '  (pad "" np_thru_hole circle (at -5.08 0) (size 1.7 1.7) (drill 1.7) (layers *.Cu *.Mask))\n'
    body += '  (pad "" np_thru_hole circle (at 0 0) (size 4 4) (drill 4) (layers *.Cu *.Mask))\n'

    # pads
    body += '  (pad 1 thru_hole circle (at -3.81 -2.54) (size 2.2 2.2) (drill 1.5) (layers *.Cu *.Mask))\n' + \
              '  (pad 2 thru_hole circle (at 2.54 -5.08) (size 2.2 2.2) (drill 1.5) (layers *.Cu *.Mask))\n'
    if isReversible:
        body += '  (pad 1 thru_hole circle (at -2.54 -5.08) (size 2.2 2.2) (drill 1.5) (layers *.Cu *.Mask))\n' + \
                  '  (pad 2 thru_hole circle (at 3.81 -2.54) (size 2.2 2.2) (drill 1.5) (layers *.Cu *.Mask))\n'

    if hasLED:
        body += '  (pad 3 thru_hole rect (at -1.27 5.08) (size 1.6 1.6) (drill 0.8) (layers *.Cu *.Mask))\n' + \
                  '  (pad 4 thru_hole circle (at 1.27 5.08) (size 1.6 1.6) (drill 0.8) (layers *.Cu *.Mask))\n'

    # 3D model
    body += '  (model ${KISYS3DMOD}/SMKJP.3dshapes/cherry_mx.step\n    (at (xyz 0 0 0))\n    (scale (xyz 1 1 1))\n    (rotate (xyz 0 0 0))\n  )\n'

    body += ')\n'

    name = f'SW_Cherry_MX1A_{unit}u_{mount}{"_LED" if hasLED else ""}{"_Reversible" if isReversible else ""}.kicad_mod'

    return name, body

if __name__ == '__main__':
    args = sys.argv
    if len(args) < 2:
        print('error: please set output path!!!')
        exit()

    path = args[1]

    for isPCB in range(2):
        for hasLED in range(2):
            for isReversible in range(2):
                for n in range(4):
                    size = 1 + n * 0.25
                    fp = generate_footprint(size, isPCB, hasLED, isReversible)
                    with open(path + "\\" + fp[0], "w") as f:
                        f.write(fp[1])
                    print(path + fp[0])

    print("done")
    exit()