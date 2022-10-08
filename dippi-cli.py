def dpi(w, h, screen_size):
    print(type(w), type(h), type(screen_size))
    return float(w)*float(h)/float(screen_size)

def result_desktop(dpi):
    dpi = float(dpi)
    if dpi < 70:
        return "Probably too low"
    elif 70 <= dpi < 90:
        return "Unclear (potentially too low) for LoDPI"
    elif 90 <= dpi < 150:
        return "Ideal for LoDPI"
    elif 150 <= dpi < 165:
        return "Unclear (potentially too high) for LoDPI"
    elif 165 <= dpi < 180:
        return "Unclear (potentially too low) for HiDPI"
    elif 180 <= dpi < 300:
        return "Ideal for HiDPI"
    elif 300 <= dpi < 340:
        return "Unclear (potentially too high) for HiDPI"
    else:
        return "Probably too high"

def result_laptop(dpi):
    if dpi < 110:
        return "Probably too low"
    elif 110 <= dpi < 124:
        return "Unclear (potentially too low) for LoDPI"
    elif 124 <= dpi < 156:
        return "Ideal for LoDPI"
    elif 156 <= dpi < 170:
        return "Unclear (potentially too high) for LoDPI"
    elif 170 <= dpi < 220:
        return "Probably too high for LoDPI or too low for HiDPI"
    elif 220 <= dpi < 248:
        return "Unclear (potentially too low) for HiDPI"
    elif 248 <= dpi < 312:
        return "Ideal for HiDPI"
    elif 312 <= dpi < 340:
        return "Unclear (potentially too high) for HiDPI"
    else:
        return "Probably too high"

def lap_or_desk(dpi):
    lap_or_desk = input('L or D')
    laptop = "laptop"
    desktop = "desktop"
    if lap_or_desk == laptop:
        return result_laptop(dpi)
    elif lap_or_desk == desktop:
        return result_desktop(dpi)
    else:
        return

def exec():
    w = input('What is the width resolution of your screen?')
    h = input('What is the height resolution of your display?')
    screen_size = input('What is your screen size?')
    dpi(w, h, screen_size)
    lap_or_desk(dpi)

print(exec())