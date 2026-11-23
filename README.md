# mb_wiki：果蠅學習與記憶知識庫

這是一座關於果蠅（*Drosophila*）學習與記憶研究的文獻知識庫。目前的主軸是蕈狀體（mushroom body）：它是果蠅腦中負責「把氣味和好壞結果連起來」的區域，是研究學習與記憶最常用的模型。本庫原本只收蕈狀體的研究，2026-11-12 起擴大到果蠅的學習與記憶，不限腦區，例如中央複合體的空間學習、求偶制約、幼蟲的學習；這些主題會在收到論文後陸續加入。讀這個庫不需要先懂神經科學：各頁裡的術語第一次出現時都有白話說明，短的參考頁可以隨時查。

本庫的頁面由 AI（Claude）閱讀論文後撰寫，人負責挑論文、提問與裁決。它不是論文摘要的堆疊：每篇論文會被拆開，重新組織到「主題」、「概念」與「實體」頁上；論文之間說法不同的地方會被標出來，而不會被抹平成一段通順的話。作法沿用本實驗室（BSC）的另一座知識庫 `research_with_AI`，原型是 Andrej Karpathy 提出的「LLM Wiki」，也就是由 AI 持續撰寫與維護一組互相連結的筆記頁。只想讀內容的人可以略過這段背景。

**網站：https://marginli.github.io/mb_wiki/**　　點開就能讀，不需要帳號。網站左側有搜尋框與全部頁面的清單，頁面之間的連結都能點。下面的閱讀順序在網站上同樣適用，例如在搜尋框輸入「蕈狀體」就能找到第一頁。

## 建議的閱讀順序

第一次來，照這個順序讀就好：

1. [蕈狀體](wiki/entities/e-mushroom-body.md)：先知道這個腦區長什麼樣（短頁）
2. [Kenyon 細胞](wiki/entities/e-kenyon-cell.md)：蕈狀體裡代表氣味的主要神經元（短頁）
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
- [t-innate-learned-integration](wiki/topics/t-innate-learned-integration.md)：先天與習得的價值在哪裡整合
- [t-mbon-to-action](wiki/topics/t-mbon-to-action.md)：學到的價值怎麼變成動作：MBON 下游的讀出
- [t-visual-learning-circuits](wiki/topics/t-visual-learning-circuits.md)：果蠅用哪一塊腦記住看到的東西
- [t-stereotypy-to-individualization](wiki/topics/t-stereotypy-to-individualization.md)：氣味代碼在哪一層不再固定

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
- [s-mao-2009-dopaminergic-neuron-types](wiki/sources/s-mao-2009-dopaminergic-neuron-types.md)：Mao 2009, *Front. Neural Circuits*
- [s-gervasi-2010-pka-dynamics](wiki/sources/s-gervasi-2010-pka-dynamics.md)：Gervasi 2010, *Neuron*
- [s-ofstad-2011-visual-place-learning](wiki/sources/s-ofstad-2011-visual-place-learning.md)：Ofstad, Zuker & Reiser 2011, *Nature*
- [s-burke-2012-octopamine-dopamine-reward](wiki/sources/s-burke-2012-octopamine-dopamine-reward.md)：Burke 2012, *Nature*
- [s-aso-2014-mb-architecture](wiki/sources/s-aso-2014-mb-architecture.md)：Aso 2014, *eLife*
- [s-aso-2014-mbon-valence](wiki/sources/s-aso-2014-mbon-valence.md)：Aso 2014, *eLife*
- [s-vogt-2014-shared-visual-olfactory-circuits](wiki/sources/s-vogt-2014-shared-visual-olfactory-circuits.md)：Vogt et al. 2014, *eLife*
- [s-dylla-2017-trace-conditioning-dan-plasticity](wiki/sources/s-dylla-2017-trace-conditioning-dan-plasticity.md)：Dylla 2017, *Front Neural Circuits*
- [s-aso-2019-nitric-oxide-cotransmitter](wiki/sources/s-aso-2019-nitric-oxide-cotransmitter.md)：Aso 2019, *eLife*
- [s-li-2020-mb-connectome](wiki/sources/s-li-2020-mb-connectome.md)：Li et al. 2020, *eLife*
- [s-eschbach-2021-learned-innate-valence-integration](wiki/sources/s-eschbach-2021-learned-innate-valence-integration.md)：Eschbach 2021, *eLife*
- [s-pribbenow-2022-postsynaptic-plasticity](wiki/sources/s-pribbenow-2022-postsynaptic-plasticity.md)：Pribbenow 2022, *eLife*
- [s-aso-2023-upwind-neurons](wiki/sources/s-aso-2023-upwind-neurons.md)：Aso 2023, *eLife*
- [s-yamada-2023-second-order-conditioning](wiki/sources/s-yamada-2023-second-order-conditioning.md)：Yamada 2023, *eLife*
- [s-ganguly-2024-visual-inputs-to-kc](wiki/sources/s-ganguly-2024-visual-inputs-to-kc.md)：Ganguly, Heckman et al. 2024, *Nature Communications*
- [s-huang-2024-dopamine-memory-dynamics](wiki/sources/s-huang-2024-dopamine-memory-dynamics.md)：Huang 2024, *Nature*
- [s-kaldun-2025-dop1r2-memory-phases](wiki/sources/s-kaldun-2025-dop1r2-memory-phases.md)：Kaldun 2025, *eLife*
- [s-tumkaya-2025-synthetic-memory-inception](wiki/sources/s-tumkaya-2025-synthetic-memory-inception.md)：Tumkaya 2025, *iScience*
- [s-minnick-2026-untrained-connectome](wiki/sources/s-minnick-2026-untrained-connectome.md)：Minnick 2026, *arXiv:*

**概念**
- [c-camp-signaling](wiki/concepts/c-camp-signaling.md)：cAMP 訊號（cAMP signaling）
- [c-coincidence-detection](wiki/concepts/c-coincidence-detection.md)：巧合偵測（coincidence detection）
- [c-cs-us-timing](wiki/concepts/c-cs-us-timing.md)：制約刺激與非制約刺激的時序（CS–US timing）
- [c-ex-vivo-explant](wiki/concepts/c-ex-vivo-explant.md)：離體全腦製備（ex vivo brain explant）
- [c-kc-mbon-plasticity](wiki/concepts/c-kc-mbon-plasticity.md)：KC→MBON 突觸可塑性（KC-MBON synaptic plasticity）
- [c-mb-compartment](wiki/concepts/c-mb-compartment.md)：蕈狀體區室（MB compartment）
- [c-memory-consolidation](wiki/concepts/c-memory-consolidation.md)：記憶鞏固與再鞏固（memory consolidation and reconsolidation）
- [c-memory-extinction](wiki/concepts/c-memory-extinction.md)：記憶消退（memory extinction）
- [c-odor-generalization](wiki/concepts/c-odor-generalization.md)：氣味類化（odor generalization）
- [c-performance-index](wiki/concepts/c-performance-index.md)：表現指數（performance index, P.I.）
- [c-presynaptic-calcium](wiki/concepts/c-presynaptic-calcium.md)：突觸前末梢的鈣（presynaptic calcium）
- [c-spaced-training](wiki/concepts/c-spaced-training.md)：間隔與集中訓練（spaced and massed training）
- [c-us-substitution](wiki/concepts/c-us-substitution.md)：以人工活化取代非制約刺激（US substitution）
- [c-whole-cell-patch-clamp](wiki/concepts/c-whole-cell-patch-clamp.md)：全細胞膜片鉗記錄（whole-cell patch clamp）
- [c-acquisition-vs-retrieval](wiki/concepts/c-acquisition-vs-retrieval.md)：獲得與提取的時段拆分（acquisition vs retrieval）
- [c-appetitive-memory](wiki/concepts/c-appetitive-memory.md)：獎賞記憶（appetitive memory）
- [c-feedforward-inhibition](wiki/concepts/c-feedforward-inhibition.md)：前饋抑制（feedforward inhibition）與 MBON 之間的抑制
- [c-neurotransmitter-prediction](wiki/concepts/c-neurotransmitter-prediction.md)：傳遞物質預測（neurotransmitter prediction）
- [c-nonassociative-learning](wiki/concepts/c-nonassociative-learning.md)：非聯結式學習（nonassociative learning）與不配對對照
- [c-octopamine-reward-signal](wiki/concepts/c-octopamine-reward-signal.md)：章魚胺訊號與獎賞假說（octopamine reward signal）
- [c-prediction-error](wiki/concepts/c-prediction-error.md)：預測誤差（prediction error）
- [c-second-order-conditioning](wiki/concepts/c-second-order-conditioning.md)：二階制約（second-order conditioning）
- [c-sparse-coding](wiki/concepts/c-sparse-coding.md)：稀疏編碼（sparse coding）
- [c-valence-coding](wiki/concepts/c-valence-coding.md)：價值編碼（valence coding）

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
- [e-mbon](wiki/entities/e-mbon.md)：蕈狀體輸出神經元（mushroom body output neuron, MBON）
- [e-mushroom-body](wiki/entities/e-mushroom-body.md)：蕈狀體（mushroom body）
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
- [e-238y-gal4](wiki/entities/e-238y-gal4.md)：238Y-GAL4 驅動品系（238Y-GAL4）
- [e-apl-neuron](wiki/entities/e-apl-neuron.md)：APL 神經元（anterior paired lateral neuron, MB-APL）
- [e-c305a-gal4](wiki/entities/e-c305a-gal4.md)：c305a-GAL4 驅動品系（c305a-GAL4）
- [e-catmaid](wiki/entities/e-catmaid.md)：CATMAID 電顯追蹤平台（CATMAID）
- [e-color-conditioning-arena](wiki/entities/e-color-conditioning-arena.md)：四象限顏色制約場地（colour conditioning arena）
- [e-dpm-neuron](wiki/entities/e-dpm-neuron.md)：DPM 神經元（dorsal paired medial neuron, MB-DPM）
- [e-dtrpa1](wiki/entities/e-dtrpa1.md)：熱活化通道（dTrpA1）
- [e-dumb2](wiki/entities/e-dumb2.md)：dumb² 等位基因（*dumb²*）
- [e-dunce](wiki/entities/e-dunce.md)：dunce 基因（dunce, dnc）
- [e-ellipsoid-body](wiki/entities/e-ellipsoid-body.md)：橢球體（ellipsoid body, EB）
- [e-gal80ts](wiki/entities/e-gal80ts.md)：溫度開關型 GAL4 抑制蛋白（Gal80<sup>ts</sup>）
- [e-grasp](wiki/entities/e-grasp.md)：跨突觸夥伴 GFP 重組（GFP Reconstitution Across Synaptic Partners, GRASP）
- [e-hemibrain](wiki/entities/e-hemibrain.md)：hemibrain 連結體資料集（hemibrain）
- [e-kir2-1](wiki/entities/e-kir2-1.md)：Kir2.1 內向整流鉀通道（Kir2.1）
- [e-mb008b](wiki/entities/e-mb008b.md)：MB008B split-GAL4 品系（MB008B）
- [e-mb247-gal4](wiki/entities/e-mb247-gal4.md)：MB247-GAL4 驅動品系（MB247-GAL4）
- [e-mbon-alpha1](wiki/entities/e-mbon-alpha1.md)：MBON-α1（α1 輸出神經元）
- [e-mbon-alpha2sc](wiki/entities/e-mbon-alpha2sc.md)：MBON-α2sc（α2sc 輸出神經元）
- [e-mbon-alpha3](wiki/entities/e-mbon-alpha3.md)：MBON-α3（α3 輸出神經元）
- [e-mcfo](wiki/entities/e-mcfo.md)：多色隨機單細胞標記（MultiColor FlpOut, MCFO）
- [e-ok107-gal4](wiki/entities/e-ok107-gal4.md)：OK107-GAL4 驅動品系（OK107-GAL4）
- [e-ppl1-alpha2alpha2](wiki/entities/e-ppl1-alpha2alpha2.md)：PPL1-α′2α2 多巴胺神經元（PPL1-α′2α2, MB-V1）
- [e-ppl1-alpha3](wiki/entities/e-ppl1-alpha3.md)：PPL1-α3 多巴胺神經元（PPL1-α3）
- [e-ppl1-alpha3prime](wiki/entities/e-ppl1-alpha3prime.md)：PPL1-α′3 多巴胺神經元（PPL1-α′3）
- [e-tnt](wiki/entities/e-tnt.md)：破傷風毒素輕鏈（TNT / TeNT / TnT / TNTe）
- [e-vt1211](wiki/entities/e-vt1211.md)：VT1211 驅動品系（VT1211-GAL4／-LexA）
- [e-accessory-calyx](wiki/entities/e-accessory-calyx.md)：副萼（accessory calyx）
- [e-fafb](wiki/entities/e-fafb.md)：FAFB 全腦電顯影像體積（FAFB）
- [e-lvin](wiki/entities/e-lvin.md)：局部視覺中間神經元（local visual interneuron, LVIN）
- [e-nblast](wiki/entities/e-nblast.md)：NBLAST 形態比對演算法（NBLAST）
- [e-neuprint](wiki/entities/e-neuprint.md)：neuPrint 連結體查詢介面（neuPrint）
- [e-visual-projection-neuron](wiki/entities/e-visual-projection-neuron.md)：視覺投射神經元（visual projection neuron, VPN）

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
