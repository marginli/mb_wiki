# mb_wiki：果蠅蘑菇體研究知識庫

這是一座關於果蠅（*Drosophila*）蘑菇體（mushroom body）研究的文獻知識庫。蘑菇體是果蠅腦中負責「把氣味和好壞結果連起來」的區域，是研究學習與記憶最常用的模型之一。讀這個庫不需要先懂神經科學：每個術語第一次出現時都有白話說明，短的參考頁可以隨時查。

本庫的頁面由 AI（Claude）閱讀論文後撰寫，人負責挑論文、提問與裁決。它不是論文摘要的堆疊：每篇論文會被拆開，重新組織到「主題」、「概念」與「實體」頁上；論文之間說法不同的地方會被標出來，而不會被抹平成一段通順的話。作法沿用本實驗室（BSC）的另一座知識庫 `research_with_AI`，原型是 Andrej Karpathy 提出的「LLM Wiki」，也就是由 AI 持續撰寫與維護一組互相連結的筆記頁。只想讀內容的人可以略過這段背景。

## 建議的閱讀順序

第一次來，照這個順序讀就好：

1. [蘑菇體](wiki/entities/e-mushroom-body.md)：先知道這個腦區長什麼樣（短頁）
2. [Kenyon 細胞](wiki/entities/e-kenyon-cell.md)：蘑菇體裡代表氣味的主要神經元（短頁）
3. [先後與間隔：氣味和多巴胺的時序如何決定學到什麼](wiki/topics/t-timing-rules.md)：第一條主題，白話文章
4. [從多巴胺到突觸改變：KC 軸突怎麼讀出增強訊號](wiki/topics/t-dopamine-to-plasticity.md)：第二條主題
5. 對某篇論文有興趣，再讀它的來源頁（見下方目錄）。來源頁先讀「為什麼重要」與「科普文」，需要細節再讀「專業文」

[index.md](index.md) 是總索引，列出每條主題底下有哪些頁。

## 全部頁面（在 GitHub 上可直接點）

頁面內部用 `[[頁名]]` 互相連結。**這種連結在 GitHub 網頁上不能點**，要回到這份目錄找同名的頁。檔名開頭代表頁的種類，也決定它放在哪個資料夾：

| 開頭 | 種類 | 資料夾 | 內容 |
|---|---|---|---|
| `t-` | 主題 | `wiki/topics/` | 把幾篇論文對同一個問題的說法串成一篇白話文章。**讀者的入口** |
| `s-` | 來源 | `wiki/sources/` | 一篇論文一頁：科普文、研究生程度的專業文、每張主圖的翻譯與解讀 |
| `c-` | 概念 | `wiki/concepts/` | 查一個術語或方法是什麼意思，以及三篇論文各怎麼用它 |
| `e-` | 實體 | `wiki/entities/` | 查一種神經元、一個腦區或一項實驗工具 |
| `syn-` | 綜述 | `wiki/synthesis/` | 本庫自己的狀態：論文之間的矛盾、沒人做過的實驗、本庫改正過自己的地方 |

**主題**
- [t-timing-rules](wiki/topics/t-timing-rules.md)：先後與間隔，氣味和多巴胺的時序如何決定學到什麼
- [t-dopamine-to-plasticity](wiki/topics/t-dopamine-to-plasticity.md)：從多巴胺到突觸改變

**來源（論文）**
- [s-tomchik-2009-camp-dynamics](wiki/sources/s-tomchik-2009-camp-dynamics.md)：Tomchik & Davis 2009, *Neuron*
- [s-hige-2015-heterosynaptic-plasticity](wiki/sources/s-hige-2015-heterosynaptic-plasticity.md)：Hige et al. 2015, *Neuron*
- [s-handler-2019-dopamine-receptor-timing](wiki/sources/s-handler-2019-dopamine-receptor-timing.md)：Handler et al. 2019, *Cell*

**概念**
- [c-cs-us-timing](wiki/concepts/c-cs-us-timing.md)：線索與增強訊號的時序
- [c-coincidence-detection](wiki/concepts/c-coincidence-detection.md)：巧合偵測
- [c-camp-signaling](wiki/concepts/c-camp-signaling.md)：cAMP 訊號
- [c-mb-compartment](wiki/concepts/c-mb-compartment.md)：蘑菇體區室
- [c-kc-mbon-plasticity](wiki/concepts/c-kc-mbon-plasticity.md)：KC→MBON 突觸可塑性
- [c-performance-index](wiki/concepts/c-performance-index.md)：表現指數（行為量法）
- [c-us-substitution](wiki/concepts/c-us-substitution.md)：以人工活化取代真實的懲罰或獎賞

**實體**
- [e-mushroom-body](wiki/entities/e-mushroom-body.md)：蘑菇體
- [e-kenyon-cell](wiki/entities/e-kenyon-cell.md)：Kenyon 細胞（KC）
- [e-dopaminergic-neuron](wiki/entities/e-dopaminergic-neuron.md)：多巴胺神經元（DAN）
- [e-mbon](wiki/entities/e-mbon.md)：蘑菇體輸出神經元（MBON）
- [e-gcamp](wiki/entities/e-gcamp.md)：GCaMP 鈣感測器
- [e-epac-camp-sensor](wiki/entities/e-epac-camp-sensor.md)：Epac 系 cAMP 感測器
- [e-cschrimson](wiki/entities/e-cschrimson.md)：CsChrimson 光遺傳通道
- [e-split-gal4](wiki/entities/e-split-gal4.md)：split-GAL4 驅動品系

**綜述與登記簿**
- [syn-contradictions](wiki/synthesis/syn-contradictions.md)：矛盾、空缺與本庫的不確定性
- [syn-changelog](wiki/synthesis/syn-changelog.md)：更新履歷
- [numbers.md](numbers.md)：數字登記簿。頁面裡的每個數字都先登記在這裡，附定義與量測方式；想查某個數字怎麼來的時候看
- [intake.md](intake.md)：收錄登記簿，每份 PDF 的處理狀態（主要給維護者）
- [log.md](log.md)：日誌，每次修改做了什麼（主要給維護者）

## 頁面裡的標記

| 標記 | 意思 |
|---|---|
| `※ 推論` | 論文沒有明說，是本庫依據論文內容推出來的，會附上依據 |
| `？待查` | 值得查證但目前沒有來源，刻意不填 |
| `⚠️ 矛盾` | **兩篇不同的論文**說法互相牴觸，等人裁決 |
| `⚠️`（後面沒有「矛盾」二字） | **同一篇論文**自己前後不一致，例如摘要和圖對不上。只記錄，不需裁決 |

## 在自己電腦上打開（選用）

只想讀內容，直接在 GitHub 網頁上看就夠了。想要頁面之間能直接點，有兩條路。**不熟電腦的話，請選第一條**，不用打任何指令。

### 不用打指令：下載 ZIP，用 Obsidian 開

Obsidian 是一個免費的筆記軟體（https://obsidian.md ），能直接讀這種 Markdown 檔案，頁面之間的 `[[ ]]` 連結都能點，還能看頁面之間的關係圖。

1. 確認你有權限。這是私有 repo，你的 GitHub 帳號要先被 repo 擁有者加為協作者，並接受 GitHub 寄來的邀請 email。如果你現在正在 GitHub 上讀這份說明，就表示已經有權限，可以跳過這一步。
2. 在 GitHub 的 repo 頁面，按綠色的「Code」按鈕，選「Download ZIP」，把下載的壓縮檔解壓縮。解壓後有時會出現「資料夾裡還有一層同名資料夾」，要用的是裡面看得到 `index.md` 的那一層。
3. 安裝並打開 Obsidian，選「Open folder as vault」（把資料夾當成筆記庫開啟），選剛才那個看得到 `index.md` 的資料夾。介面若是中文，這個選項會是對應的中文名稱。
4. 從 `index.md` 開始讀。

缺點是 ZIP 不會自動更新；知識庫有新內容時，要重新下載一次。

### 開成網站：需要用終端機

這條路能全文搜尋，也能用 `git pull` 隨時更新。需要用到終端機，也就是輸入文字指令的視窗：macOS 是「應用程式 → 工具程式 → 終端機」，Linux 是 Terminal。Windows 請先安裝 WSL（Windows Subsystem for Linux，讓 Windows 能執行 Linux 指令）：在開始選單搜尋「PowerShell」，以系統管理員身分開啟，輸入 `wsl --install`，完成後重新開機，再從開始選單打開「Ubuntu」，之後的指令都在這個視窗裡輸入。

**1. 確認工具。** 在終端機輸入以下兩行，各自印出版本號碼就表示已安裝：

```bash
git --version
python3 --version
```

沒有的話：macOS 到 https://git-scm.com 與 https://www.python.org 安裝；Linux 與 WSL 的 Ubuntu 輸入 `sudo apt install git python3-pip`。另外要安裝 GitHub 的命令列工具 `gh`，各系統的安裝方式在 https://cli.github.com 。Windows 使用者要照其中 Linux 的說明，在 Ubuntu 視窗裡安裝，不是安裝 Windows 版。

**2. 登入並下載。** 第一次使用 `gh` 時執行一次 `gh auth login`，依提示選 GitHub.com、HTTPS、用瀏覽器登入。接著下載 repo。指令裡的「擁有者帳號」，就是 repo 網址 `https://github.com/擁有者帳號/mb_wiki` 中間那一段，可以從瀏覽器網址列複製。

```bash
gh auth login                        # 第一次才需要
gh repo clone 擁有者帳號/mb_wiki       # 下載到目前所在的資料夾
cd mb_wiki                           # 進入剛下載的資料夾
```

**3. 開成網站。**

```bash
pip install markdown pillow     # 第一次需要
./tools/serve.sh                # 產生網站並啟動；保持這個視窗開著
```

成功時，終端機會印出 `→ http://127.0.0.1:8788/index.html`。腳本不會自動開瀏覽器，請自己打開瀏覽器前往這個網址，會看到左側有搜尋框與頁面清單的網站。看完在終端機按 Ctrl-C 結束。之後要取得新內容，在 `mb_wiki` 資料夾裡輸入 `git pull`。

**如果出錯：**

| 狀況 | 改用 |
|---|---|
| `./tools/serve.sh` 顯示權限不足 | `bash tools/serve.sh` |
| 找不到 `pip`，或 `pip install` 被系統拒絕 | `python3 -m pip install --user markdown pillow` |
| 8788 埠已被占用 | `./tools/serve.sh 9000`，再開 `http://127.0.0.1:9000/` |

## 版權

`papers/` 內的 PDF 與 `assets/` 內從論文擷取的圖，版權屬原出版社。這些論文可免費下載，但「可以免費讀」不等於「可以再散布」。**本 repo 為私有，只開放給受邀的同事，請勿轉為公開或轉傳。** 若日後要公開，先把非 CC 授權的 PDF 與原圖移出 repo。

## 想加論文或協作（只讀者可略過）

規則全部寫在 [CLAUDE.md](CLAUDE.md)。收錄新論文需要 Claude Code（Anthropic 的 AI 程式助理，需自己的帳號）。流程是：把 PDF 放進 `papers/`，在 repo 根目錄開 Claude Code，說「更新」。Claude 會先跑對帳腳本找出新論文，再依 `.claude/skills/ingest-paper/` 的流程收錄，並回頭改寫受影響的主題頁。

```bash
python3 tools/scan.py      # 哪些 PDF 還沒收錄、有沒有重複或不一致
python3 tools/links.py     # 頁面之間有沒有壞連結
```
