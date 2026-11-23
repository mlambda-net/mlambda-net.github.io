#!/usr/bin/env python3
"""script/products.py -- lay MLambda.Docs's products/ into the site before Jekyll builds it.

    python3 script/products.py [<products folder>]

The folder defaults to $DOCS_PRODUCTS, else ../../docs/products (the site inside a MLambda.Genesis checkout, at
personal/mlambda-net.github.io). CI checks MLambda.Docs out into _docs and passes _docs/products.

- Every .md becomes a document of the `products` collection (_products/<path>.md), published at
  /products/<path>.html. A README.md is its folder's page: its front matter names its permalink, and the catalog's
  (products/README.md) is given /products/ and the catalog layout here.
- Every other file (pictures, mostly) is copied to products/<path> and served as it is.
- A link to a page (`x.md`, `../y/README.md#part`) is rewritten to the page's address, relative as it was written.
- A link into a private repository of the family (github.com/mlambda-net/MLambda.*) keeps its words and loses its
  address: visitors cannot open it.

_products/ and products/ are written here, never edited by hand, and ignored by git.
"""
import os
import re
import shutil
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LINK = re.compile(r"(!?\[[^\]]*\]\()([^)\s]+)(\))")
PRIVATE = re.compile(r"\[([^\]]*)\]\(https?://github\.com/mlambda-net/MLambda[^)]*\)")


def address(target):
    if re.match(r"^([a-z]+:|#|/)", target):
        return target
    path, hash_, fragment = target.partition("#")
    if not path.endswith(".md"):
        return target
    if os.path.basename(path) == "README.md":
        folder = os.path.dirname(path)
        page = folder + "/" if folder else "./"
    else:
        page = path[:-3] + ".html"
    return page + hash_ + fragment


def hero(text):
    """The picture a page's front matter names as its `image`: the product layout shows it in the hero."""
    m = re.match(r"---\n(.*?)\n---\n", text, re.S)
    found = m and re.search(r"^image:\s*(\S+)\s*$", m.group(1), re.M)
    return found.group(1) if found else None


def rewrite(text):
    text = PRIVATE.sub(lambda m: m.group(1), text)
    shown = hero(text)
    if shown:
        # the hero shows it already: the body's first line holding only that picture is dropped
        text = re.sub(r"^!\[[^\]]*\]\(" + re.escape(shown) + r"\)\n\n?", "", text, count=1, flags=re.M)
    out, fenced = [], False
    for line in text.splitlines(keepends=True):
        if line.lstrip().startswith("```"):
            fenced = not fenced
        out.append(line if fenced else LINK.sub(lambda m: m.group(1) + address(m.group(2)) + m.group(3), line))
    return "".join(out)


def main():
    default = os.path.join(ROOT, "..", "..", "docs", "products")
    source = os.path.abspath(sys.argv[1] if len(sys.argv) > 1 else os.environ.get("DOCS_PRODUCTS", default))
    if not os.path.isdir(source):
        sys.exit(f"script/products.py: no products folder at {source}")
    pages, files = os.path.join(ROOT, "_products"), os.path.join(ROOT, "products")
    for folder in (pages, files):
        shutil.rmtree(folder, ignore_errors=True)
    counted = {"pages": 0, "files": 0}
    for base, dirs, names in os.walk(source):
        dirs[:] = sorted(d for d in dirs if not d.startswith("."))
        for name in sorted(names):
            if name.startswith("."):
                continue
            src = os.path.join(base, name)
            rel = os.path.relpath(src, source).replace(os.sep, "/")
            if rel.endswith(".md"):
                with open(src, encoding="utf-8") as f:
                    text = rewrite(f.read())
                if not text.startswith("---\n"):
                    sys.exit(f"script/products.py: {rel} has no front matter")
                if rel == "README.md":
                    text = text.replace("---\n", "---\nlayout: catalog\npermalink: /products/\n", 1)
                dst = os.path.join(pages, rel)
                counted["pages"] += 1
                os.makedirs(os.path.dirname(dst), exist_ok=True)
                with open(dst, "w", encoding="utf-8", newline="\n") as f:
                    f.write(text)
            else:
                dst = os.path.join(files, rel)
                counted["files"] += 1
                os.makedirs(os.path.dirname(dst), exist_ok=True)
                shutil.copyfile(src, dst)
    print(f"script/products.py: {counted['pages']} pages and {counted['files']} files from {source}")


if __name__ == "__main__":
    main()
