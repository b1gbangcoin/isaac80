from PIL import Image, ImageSequence
import sys
import os

def make_nine_grid_gif(gif_paths, jpg_path, out_gif_path, cell_size=200):
    gif_list = [Image.open(p) for p in gif_paths]
    jpg_img = Image.open(jpg_path).convert("RGBA")
    jpg_img = jpg_img.resize((cell_size, cell_size))

    gif_frames = []
    for g in gif_list:
        frames = []
        for f in ImageSequence.Iterator(g):
            frames.append(f.convert("RGBA").resize((cell_size, cell_size)))
        gif_frames.append(frames)

    max_frame = max(len(fs) for fs in gif_frames)
    out_frames = []

    pos_map = [
        (0, 0),
        (0, 2),
        (1, 1),
        (2, 0),
        (2, 2)
    ]
    rest_pos = [(0,1),(1,0),(1,2),(2,1)]

    for frame_idx in range(max_frame):
        canvas = Image.new("RGBA", (cell_size*3, cell_size*3))
        for i, (r, c) in enumerate(pos_map):
            fs = gif_frames[i]
            fi = frame_idx % len(fs)
            canvas.paste(fs[fi], (c*cell_size, r*cell_size))
        for r,c in rest_pos:
            canvas.paste(jpg_img, (c*cell_size, r*cell_size))
        out_frames.append(canvas)

    out_frames[0].save(
        out_gif_path,
        save_all=True,
        append_images=out_frames[1:],
        duration=100,
        loop=0,
        disposal=2
    )

if __name__ == "__main__":
    script_dir = os.path.dirname(os.path.abspath(__file__))

    if len(sys.argv) == 2:
        jpg_path = sys.argv[1]
        out_gif_path = os.path.splitext(jpg_path)[0] + "_result.gif"
    elif len(sys.argv) == 3:
        jpg_path = sys.argv[1]
        out_gif_path = sys.argv[2]
    else:
        print("用法:")
        print("  python3 ninegrid_gif.py <input.jpg>")
        print("  python3 ninegrid_gif.py <input.jpg> <output.gif>")
        sys.exit(1)

    gif_files = [
        os.path.join(script_dir, "g1.gif"),
        os.path.join(script_dir, "g2.gif"),
        os.path.join(script_dir, "g3.gif"),
        os.path.join(script_dir, "g4.gif"),
        os.path.join(script_dir, "g5.gif")
    ]

    for g in gif_files:
        if not os.path.exists(g):
            print(f"错误: 找不到 {g}")
            sys.exit(1)

    if not os.path.exists(jpg_path):
        print(f"错误: 找不到 {jpg_path}")
        sys.exit(1)

    make_nine_grid_gif(gif_files, jpg_path, out_gif_path, cell_size=200)
    print(f"✓ 成功生成: {out_gif_path}")

