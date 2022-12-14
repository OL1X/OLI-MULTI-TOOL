LICENSE = """
Copyright © 2022 OLI
Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the “Software”), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
"""

from colored import fg

r = fg(255) # Setup color variables
r2 = fg(255)
b = fg(32)
w = fg(15)

def show_credits():
    print(f"\n {r2}[{b}+{r2}] Author: OLI")
    print(f" {r2}[{b}+{r2}] Discord : OL#5555 | LL#5555")
    print(f" {r2}[{b}+{r2}] AFN TEAM Discord Server: https://discord.gg/f8GrpafgBg")
    print(f" {r2}[{b}+{r2}] OLI'S INSTGRAM : https://www.instagram.com/2azko/ ")
    print(f" {r2}[{b}+{r2}] AFN TEAM's INSTGRAM : https://www.instagram.com/afn_tteam/ ")

def show_help():
    pass
