# mb_wiki：果蠅蘑菇體研究知識庫

這是一座關於果蠅（*Drosophila*）蘑菇體（mushroom body）研究的文獻知識庫。蘑菇體是果蠅腦中負責「把氣味和好壞結果連起來」的區域，是研究學習與記憶最常用的模型之一。讀這個庫不需要先懂神經科學：每個術語第一次出現時都有白話說明，短的參考頁可以隨時查。

本庫的頁面由 AI（Claude）閱讀論文後撰寫，人負責挑論文、提問與裁決。它不是論文摘要的堆疊：每篇論文會被拆開，重新組織到「主題」、「概念」與「實體」頁上；論文之間說法不同的地方會被標出來，而不會被抹平成一段通順的話。作法沿用本實驗室（BSC）的另一座知識庫 `research_with_AI`，原型是 Andrej Karpathy 提出的「LLM Wiki」，也就是由 AI 持續撰寫與維護一組互相連結的筆記頁。只想讀內容的人可以略過這段背景。

**網站：https://marginli.github.io/mb_wiki/**　　點開就能讀，不需要帳號，頁面之間的連結都能點，也能全文搜尋。

## 建議的閱讀順序

第一次來，照這個順序讀就好：

1. [蘑菇體](wiki/entities/e-mushroom-body.md)：先知道這個腦區長什麼樣（短頁）
2. [Kenyon 細胞](wiki/entities/e-kenyon-cell.md)：蘑菇體裡代表氣味的主要神經元（短頁）
3. [先後與間隔：氣味和多巴胺的時序如何決定學到什麼](wiki/topics/t-timing-rules.md)：第一條主題，白話文章
4. [從多巴胺到突觸改變：KC 軸突怎麼讀出增強訊號](wiki/topics/t-dopamine-to-plasticity.md)：第二條主題
5. 對某篇論文有興趣，再讀它的來源頁（見下方目錄）。來源頁先讀「為什麼重要」與「科普文」，需要細節再讀「專業文」

[index.md](index.md) 是總索引，列出每條主題底下有哪些頁。

## 全部頁面（在 GitHub 上也能直接點）

頁面內部用 `[[頁名]]` 互相連結。在網站上都能點；**在 GitHub 網頁上不能點**，要回到這份目錄找同名的頁。檔名開頭代表頁的種類，也決定它放在哪個資料夾：

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

## 其他看法（選用）

一般讀者用上面的網站就好。以下給想離線閱讀或協助維護的人。

**用 Obsidian 離線讀，不用打指令。** Obsidian 是一個免費的筆記軟體（https://obsidian.md ），能直接讀這種 Markdown 檔案。在本 repo 的 GitHub 頁面按綠色的「Code」按鈕，選「Download ZIP」並解壓縮（若出現兩層同名資料夾，用看得到 `index.md` 的那一層）。在 Obsidian 選「Open folder as vault」（中文介面為對應的中文選項），選那個資料夾即可。ZIP 不會自動更新，有新內容時要重新下載。

**在自己電腦上預覽網站（維護者用）。** 需要 git、Python 3，以及在終端機輸入指令：

```bash
git clone https://github.com/marginli/mb_wiki.git
cd mb_wiki
pip install markdown pillow     # 第一次需要；被拒絕時改用 python3 -m pip install --user markdown pillow
./tools/serve.sh                # 終端機會印出網址，用瀏覽器打開 http://127.0.0.1:8788/
```

看完在終端機按 Ctrl-C 結束。8788 埠被占用時，改用 `./tools/serve.sh 9000`。

## 版權

- **全文：** 本庫不放論文全文。每篇論文的來源頁都附 PMC（美國國家醫學圖書館的免費全文庫）連結，請由那裡閱讀。
- **圖片：** `assets/` 裡的圖擷取自原論文，版權屬原出版社（目前三篇都是 Elsevier）。本庫以教學與評論目的引用，每張圖下方都標明出處，這不代表出版社授權。若要在別處使用這些圖，請向出版社取得授權。
- **文字：** 頁面上的中文說明、解讀與比較是本庫自己寫的。

## 想加論文或協作（只讀者可略過）

規則全部寫在 [CLAUDE.md](CLAUDE.md)。收錄新論文需要 Claude Code（Anthropic 的 AI 程式助理，需自己的帳號），以及 repo 的寫入權限。流程是：把 PDF 放進 `papers/`（PDF 只留在自己電腦，不會進 git），在 repo 根目錄開 Claude Code，說「更新」。推上 GitHub 後，網站會在幾分鐘內自動更新。Claude 會先跑對帳腳本找出新論文，再依 `.claude/skills/ingest-paper/` 的流程收錄，並回頭改寫受影響的主題頁。

```bash
python3 tools/scan.py      # 哪些 PDF 還沒收錄、有沒有重複或不一致
python3 tools/links.py     # 頁面之間有沒有壞連結
```
