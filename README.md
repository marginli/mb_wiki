# mb_wiki：果蠅蘑菇體研究知識庫

這是一座關於果蠅（*Drosophila*）蘑菇體（mushroom body）研究的文獻知識庫。蘑菇體是果蠅腦中負責「把氣味和好壞結果連起來」的區域，是研究學習與記憶最常用的模型之一。讀這個庫不需要先懂神經科學：各頁裡的術語第一次出現時都有白話說明，短的參考頁可以隨時查。

本庫的頁面由 AI（Claude）閱讀論文後撰寫，人負責挑論文、提問與裁決。它不是論文摘要的堆疊：每篇論文會被拆開，重新組織到「主題」、「概念」與「實體」頁上；論文之間說法不同的地方會被標出來，而不會被抹平成一段通順的話。作法沿用本實驗室（BSC）的另一座知識庫 `research_with_AI`，原型是 Andrej Karpathy 提出的「LLM Wiki」，也就是由 AI 持續撰寫與維護一組互相連結的筆記頁。只想讀內容的人可以略過這段背景。

**網站：https://marginli.github.io/mb_wiki/**　　點開就能讀，不需要帳號。網站左側有搜尋框與全部頁面的清單，頁面之間的連結都能點。下面的閱讀順序在網站上同樣適用，例如在搜尋框輸入「蘑菇體」就能找到第一頁。

## 建議的閱讀順序

第一次來，照這個順序讀就好：

1. [蘑菇體](wiki/entities/e-mushroom-body.md)：先知道這個腦區長什麼樣（短頁）
2. [Kenyon 細胞](wiki/entities/e-kenyon-cell.md)：蘑菇體裡代表氣味的主要神經元（短頁）
3. [先後與間隔：氣味和多巴胺的時序如何決定學到什麼](wiki/topics/t-timing-rules.md)：第一條主題，白話文章
4. [從多巴胺到突觸改變：KC 軸突怎麼讀出增強訊號](wiki/topics/t-dopamine-to-plasticity.md)：第二條主題
5. [記憶怎麼被改寫：消退、再鞏固與新舊記憶並存](wiki/topics/t-memory-updating.md)與[輸出神經元回頭指揮多巴胺神經元](wiki/topics/t-mbon-dan-feedback.md)：記憶寫下之後發生什麼事
6. 對某篇論文有興趣，再讀它的來源頁（見下方目錄的「來源（論文）」）。來源頁先讀「為什麼重要」與「科普文」，需要細節再讀「專業文」

[index.md](index.md) 是總索引，列出每條主題底下有哪些頁。

## 全部頁面（在 GitHub 上也能直接點）

本頁的連結在 GitHub 上都能點。但點進各頁之後，頁面內文用 `[[頁名]]` 互相連結，這種連結在網站上能點，**在 GitHub 網頁上不能點**，要回到這份目錄找同名的頁。檔名開頭代表頁的種類，也決定它放在哪個資料夾：

| 開頭 | 種類 | 資料夾 | 內容 |
|---|---|---|---|
| `t-` | 主題 | `wiki/topics/` | 把幾篇論文對同一個問題的說法串成一篇白話文章。**讀者的入口** |
| `s-` | 來源 | `wiki/sources/` | 一篇論文一頁：科普文、研究生程度的專業文、每張主圖的翻譯與解讀 |
| `c-` | 概念 | `wiki/concepts/` | 查一個術語或方法是什麼意思，以及庫內各篇論文怎麼用它 |
| `e-` | 實體 | `wiki/entities/` | 查一種神經元、一個腦區或一項實驗工具 |
| `syn-` | 綜述 | `wiki/synthesis/` | 本庫自己的狀態：論文之間的矛盾、沒人做過的實驗、本庫改正過自己的地方 |

**主題**
- [t-dopamine-to-plasticity](wiki/topics/t-dopamine-to-plasticity.md)：從多巴胺到突觸改變：KC 軸突怎麼讀出增強訊號
- [t-mbon-dan-feedback](wiki/topics/t-mbon-dan-feedback.md)：輸出神經元回頭指揮多巴胺神經元：MBON→DAN 回饋迴路
- [t-memory-updating](wiki/topics/t-memory-updating.md)：記憶怎麼被改寫：消退、再鞏固與新舊記憶並存
- [t-timing-rules](wiki/topics/t-timing-rules.md)：先後與間隔：氣味和多巴胺的時序如何決定學到什麼

**來源（論文，依發表年）**
- [s-tully-1985-classical-conditioning](wiki/sources/s-tully-1985-classical-conditioning.md)：Tully & Quinn 1985, *J Comp Physiol A*
- [s-tomchik-2009-camp-dynamics](wiki/sources/s-tomchik-2009-camp-dynamics.md)：Tomchik & Davis 2009, *Neuron*
- [s-hige-2015-heterosynaptic-plasticity](wiki/sources/s-hige-2015-heterosynaptic-plasticity.md)：Hige et al. 2015, *Neuron*
- [s-cohn-2015-coordinated-neuromodulation](wiki/sources/s-cohn-2015-coordinated-neuromodulation.md)：Cohn, Morantte & Ruta 2015, *Cell*
- [s-ichinose-2015-reward-recurrent-circuit](wiki/sources/s-ichinose-2015-reward-recurrent-circuit.md)：Ichinose et al. 2015, *eLife*
- [s-aso-2016-dan-cell-type-rules](wiki/sources/s-aso-2016-dan-cell-type-rules.md)：Aso & Rubin 2016, *eLife*
- [s-felsenberg-2017-re-evaluation](wiki/sources/s-felsenberg-2017-re-evaluation.md)：Felsenberg et al. 2017, *Nature*
- [s-felsenberg-2018-memory-extinction](wiki/sources/s-felsenberg-2018-memory-extinction.md)：Felsenberg et al. 2018, *Cell*
- [s-handler-2019-dopamine-receptor-timing](wiki/sources/s-handler-2019-dopamine-receptor-timing.md)：Handler et al. 2019, *Cell*

**概念**
- [c-camp-signaling](wiki/concepts/c-camp-signaling.md)：cAMP 訊號（cAMP signaling）
- [c-coincidence-detection](wiki/concepts/c-coincidence-detection.md)：巧合偵測（coincidence detection）
- [c-cs-us-timing](wiki/concepts/c-cs-us-timing.md)：制約刺激與非制約刺激的時序（CS–US timing）
- [c-ex-vivo-explant](wiki/concepts/c-ex-vivo-explant.md)：離體全腦製備（ex vivo brain explant）
- [c-kc-mbon-plasticity](wiki/concepts/c-kc-mbon-plasticity.md)：KC→MBON 突觸可塑性（KC-MBON synaptic plasticity）
- [c-mb-compartment](wiki/concepts/c-mb-compartment.md)：蘑菇體區室（MB compartment）
- [c-memory-consolidation](wiki/concepts/c-memory-consolidation.md)：記憶鞏固與再鞏固（memory consolidation and reconsolidation）
- [c-memory-extinction](wiki/concepts/c-memory-extinction.md)：記憶消退（memory extinction）
- [c-odor-generalization](wiki/concepts/c-odor-generalization.md)：氣味類化（odor generalization）
- [c-performance-index](wiki/concepts/c-performance-index.md)：表現指數（performance index, P.I.）
- [c-presynaptic-calcium](wiki/concepts/c-presynaptic-calcium.md)：突觸前末梢的鈣（presynaptic calcium）
- [c-spaced-training](wiki/concepts/c-spaced-training.md)：間隔與集中訓練（spaced and massed training）
- [c-us-substitution](wiki/concepts/c-us-substitution.md)：以人工活化取代非制約刺激（US substitution）
- [c-whole-cell-patch-clamp](wiki/concepts/c-whole-cell-patch-clamp.md)：全細胞膜片鉗記錄（whole-cell patch clamp）

**實體**
- [e-c739-gal4](wiki/entities/e-c739-gal4.md)：c739-GAL4 驅動品系（c739-GAL4）
- [e-cschrimson](wiki/entities/e-cschrimson.md)：CsChrimson（紅光活化通道）
- [e-dopamine-receptor](wiki/entities/e-dopamine-receptor.md)：KC 上的多巴胺受體（dopamine receptors DopR1／DopR2）
- [e-dopaminergic-neuron](wiki/entities/e-dopaminergic-neuron.md)：多巴胺神經元（dopaminergic neuron, DAN）
- [e-epac-camp-sensor](wiki/entities/e-epac-camp-sensor.md)：Epac 系 cAMP 感測器（Epac-based cAMP sensor）
- [e-gcamp](wiki/entities/e-gcamp.md)：GCaMP 系鈣感測器（GCaMP calcium indicators）
- [e-kenyon-cell](wiki/entities/e-kenyon-cell.md)：Kenyon 細胞（Kenyon cell, KC）
- [e-mb099c](wiki/entities/e-mb099c.md)：MB099C 驅動品系（MB099C split-GAL4）
- [e-mb504b](wiki/entities/e-mb504b.md)：MB504B 驅動品系（MB504B split-GAL4）
- [e-mbon-gamma1pedc](wiki/entities/e-mbon-gamma1pedc.md)：MBON-γ1pedc（MVP2）
- [e-mbon-gamma2alpha1](wiki/entities/e-mbon-gamma2alpha1.md)：MBON-γ2α′1（γ2α′1 輸出神經元）
- [e-mbon-gamma4](wiki/entities/e-mbon-gamma4.md)：γ4 輸出神經元（γ4 MBON）
- [e-mbon-gamma5beta2a](wiki/entities/e-mbon-gamma5beta2a.md)：MBON-γ5β′2a（M6；γ5 MBON）
- [e-mbon](wiki/entities/e-mbon.md)：蘑菇體輸出神經元（mushroom body output neuron, MBON）
- [e-mushroom-body](wiki/entities/e-mushroom-body.md)：蘑菇體（mushroom body）
- [e-olfactory-arena](wiki/entities/e-olfactory-arena.md)：四象限光遺傳嗅覺競技場（optogenetic olfactory arena）
- [e-p2x2](wiki/entities/e-p2x2.md)：ATP 門控通道 P2X2（化學活化，chemogenetic activation）
- [e-pam-alpha1](wiki/entities/e-pam-alpha1.md)：PAM-α1 多巴胺神經元（PAM-α1）
- [e-ppl1-gamma1pedc](wiki/entities/e-ppl1-gamma1pedc.md)：PPL1-γ1pedc 多巴胺神經元（PPL1-γ1pedc, MB-MP1）
- [e-ppl1-gamma2alpha1](wiki/entities/e-ppl1-gamma2alpha1.md)：PPL1-γ2α′1 多巴胺神經元（PPL1-γ2α′1, MB-MV1）
- [e-r58e02](wiki/entities/e-r58e02.md)：R58E02 驅動品系（R58E02 driver lines）
- [e-rutabaga](wiki/entities/e-rutabaga.md)：*rutabaga* 基因與突變株（rutabaga）
- [e-shibire-ts](wiki/entities/e-shibire-ts.md)：溫度敏感型阻斷工具（shibire^ts1）
- [e-split-gal4](wiki/entities/e-split-gal4.md)：split-GAL4 驅動品系（split-GAL4 driver lines）
- [e-t-maze](wiki/entities/e-t-maze.md)：T 迷宮（T-maze）
- [e-th-gal4](wiki/entities/e-th-gal4.md)：TH-GAL4 與 TH＋DDC 驅動（TH-GAL4 and TH/DDC drivers）

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

**用 Obsidian 離線讀，不用打指令。** Obsidian 是一個免費的筆記軟體（https://obsidian.md ），能直接讀這種 Markdown 檔案。在本 repo 的 GitHub 頁面按綠色的「Code」按鈕，選「Download ZIP」並解壓縮（若出現兩層同名資料夾，用看得到 `index.md` 的那一層）。在 Obsidian 選「Open folder as vault」（把資料夾當成 Obsidian 的筆記庫開啟；中文介面為對應的中文選項），選那個資料夾即可。ZIP 不會自動更新，有新內容時要重新下載。

**在自己電腦上預覽網站（維護者用）。** 需要 git、Python 3，以及在終端機輸入指令：

```bash
git clone https://github.com/marginli/mb_wiki.git
cd mb_wiki
pip install markdown pillow     # 第一次需要；被拒絕時改用 python3 -m pip install --user markdown pillow
./tools/serve.sh                # 終端機會印出網址，用瀏覽器打開 http://127.0.0.1:8788/
```

看完在終端機按 Ctrl-C 結束。8788 埠被占用時，改用 `./tools/serve.sh 9000`。

## 版權

- **全文：** 本庫不放論文全文。每篇論文的來源頁都附 PMC（美國國家醫學圖書館的免費全文庫）連結，請由那裡閱讀。唯一的例外是 Tully & Quinn 1985：它沒有免費全文，來源頁只附 DOI（出版社的付費頁面）。
- **圖片：** `assets/` 裡的圖擷取自原論文。授權分兩類，每張圖下方的出處行都寫明是哪一類：
  - **出版社持有版權**（Tomchik 2009、Hige 2015、Cohn 2015、Handler 2019 屬 Elsevier；Felsenberg 2017 屬 Springer Nature；Tully 1985 屬 Springer-Verlag）：本庫以教學與評論目的引用，這不代表出版社授權。若要在別處使用這些圖，請向出版社取得授權。
  - **CC BY 授權**（Ichinose 2015、Aso & Rubin 2016、Felsenberg 2018）：標明原作者與出處即可自由使用。
- **文字：** 頁面上的中文說明、解讀與比較是本庫自己寫的。

## 想加論文或協作（只讀者可略過）

規則全部寫在 [CLAUDE.md](CLAUDE.md)。收錄新論文需要 Claude Code（Anthropic 的 AI 程式助理，需自己的帳號），以及 repo 的寫入權限。流程是：把 PDF 放進 `papers/`（PDF 只留在自己電腦，不會進 git），在 repo 根目錄開 Claude Code，說「更新」。推上 GitHub 後，網站會在幾分鐘內自動更新。Claude 會先跑對帳腳本找出新論文，再依 `.claude/skills/ingest-paper/` 的流程收錄，並回頭改寫受影響的主題頁。

```bash
python3 tools/scan.py      # 哪些 PDF 還沒收錄、有沒有重複或不一致
python3 tools/links.py     # 頁面之間有沒有壞連結
```
