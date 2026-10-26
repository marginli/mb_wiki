---
title: T 迷宮（T-maze）
created: 2026-10-25
updated: 2026-10-26
tags: [entity, active, cross-domain]
confidence: high
---

# T 迷宮（T-maze）


**本頁用語**（每頁可單獨查閱，故重複列出）：

- **蘑菇體（mushroom body）**：果蠅腦中把氣味和好壞經驗連起來的構造。代表氣味的 Kenyon 細胞（KC）把軸突成束排成幾條「葉」（α、α′、β、β′、γ），每條葉沿長度切成一格一格的「區室」（例如 γ1pedc、γ2、α1）；細胞以所在區室命名。見 [[e-mushroom-body]]、[[c-mb-compartment]]。
- **DAN、PAM、PPL1**：多巴胺神經元（dopaminergic neuron）送出代表懲罰或獎賞的多巴胺；PAM 群多傳遞獎賞，PPL1 群（Handler 2019 寫作 PPL）多傳遞懲罰。
- **MBON**：蘑菇體輸出神經元，接收 KC 的訊號、推動果蠅靠近或走開；學習改變的是 KC→MBON 突觸的強弱。
- **CS+／CS−、順向／逆向**：訓練時配了糖、電擊或 DAN 活化的氣味（CS+），與沒配的對照氣味（CS−）。順向配對＝氣味先、多巴胺後；逆向配對＝多巴胺先、氣味後。
- **PI（表現指數）、LI 或 Λ（學習指數）**：行為分數。一群果蠅在兩種氣味間選擇，換算成一個數；多數篇落在 −1 到 +1（Hige 2015 的刻度不同），0＝沒有偏好，正負號的意思各篇不同（見 [[c-performance-index]]）。
- **OCT、MCH**：3-辛醇（3-octanol）與 4-甲基環己醇（4-methylcyclohexanol），本庫 T 迷宮最常用的一對訓練氣味。
- **trace 制約**：氣味結束後空白一段時間才給電擊；逆向＝先電擊、後給氣味。
- **消退、再鞏固**：學會後再聞 CS+ 卻沒有糖或電擊，學到的反應減弱，叫消退（[[c-memory-extinction]]）；記憶被叫出來後暫時變得不穩定、再重新存好，叫再鞏固（[[c-memory-consolidation]]）。
- **驅動品系**：讓外加基因只在選定神經元表現的果蠅品系。GAL4 與 LexA 是兩套互不干擾的開關；split-GAL4 把 GAL4 拆成兩半（AD 與 DBD），兩半都在的細胞才有作用（[[e-split-gal4]]）。基因型寫「X/+」表示只帶一個品系的對照組。
- **活化與阻斷工具**：CsChrimson 照紅光讓神經元放電（[[e-cschrimson]]）；P2X2 遇到 ATP 讓神經元放電（[[e-p2x2]]）；shibire^ts1（shi）升溫時暫時關掉神經元的輸出（[[e-shibire-ts]]），全程維持低溫的「允許溫度對照」用來排除品系本身的效果。
- **讀數與製備**：ΔF/F0＝螢光相對刺激前基線的變化比例（0.5＝亮了 50%），以遇鈣變亮的 GCaMP 量神經元活動（[[e-gcamp]]）；離體＝把腦取出泡在養液裡做實驗（[[c-ex-vivo-explant]]），活體＝活果蠅固定後打開頭殼看。
- **標記**：※ 推論＝本庫推得、原文沒明說；？待查＝要靠其他資料確認；「從圖判讀」＝從圖上估讀的值；「text.txt 第 N 行」＝本庫保存的論文全文文字檔的行號；「該頁」指表格同一列的來源頁。

## 是什麼

測果蠅學到什麼的標準裝置：一群果蠅被送到 T 字形岔路的中央，兩條岔路各通一種氣味，讓牠們在限定時間內選邊，再數兩邊各有幾隻，換算成一個分數（表現指數，見 [[c-performance-index]]）。訓練通常也在同一套管子裡進行：讓果蠅聞一個氣味時給電擊或糖（CS+），聞另一個時不給（CS−）。一次測驗得到的是**一群**果蠅的一個分數，所以統計的 n 是「群」不是「隻」。本庫另有一種不同的裝置，四象限嗅覺競技場，見 [[e-olfactory-arena]]。

**來源。** 本庫最早的一篇是 [[s-tully-1985-classical-conditioning]]：作者把 Quinn et al. 1974 的「工具性」範式（果蠅自己走進某個氣味才挨電）改成「古典制約」（不論果蠅做什麼，氣味與電擊都照表給）；作者的理由是舊範式只讓約三分之二的果蠅躲開被電的氣味，而且挨不挨電取決於果蠅自己往哪走，難以分辨改變是不是來自「氣味＋電擊」的聯想（該頁科普文）。裝置改自 Dudai et al. 1976 的選擇室。訓練管內壁 95% 鋪電網；訓練完把果蠅敲進一個可滑動的中央小室，滑塊推到兩根收集管的交會點，就成了「T 迷宮」的選擇點，果蠅不必再被吸取或麻醉（該頁圖 1）。測驗時兩臂各有一股帶氣味的氣流從遠端流向中央，果蠅在岔路口同時聞到兩股氣味，走進哪一臂就是選了那一臂的氣味、離開另一個（該頁圖 1 解讀）；所以論文把走進 OCT 臂的果蠅算成「躲開 MCH」，走進 MCH 臂的算成「躲開 OCT」（PDF 第 266 頁）。2 分鐘內沒走進任何一臂、留在中央小室的果蠅（通常 5–10 隻）另外目視計數。分數 Λ 的算法，論文自述「如 Quinn et al.（1974）」（PDF 第 266 頁），不是本篇新創。後來各篇的協定在電壓、時序、隻數、氣味稀釋上都與本篇不同（見下表），**不能把本篇的參數當成本庫各篇的共同協定**。

## 版本與規模（各篇的協定）

| 來源 | 增強訊號與訓練時序 | 氣味 | 每群 | 測驗 | 分數 |
|---|---|---|---|---|---|
| Tully 1985 | 電擊 60 V、1.25 s，每 5 s 一下，在 CS+ 的 60 s 內共 12 下。一個訓練循環＝空白 90 s → CS+ 60 s → 空白 30 s → CS− 60 s → 空白 30 s | OCT、MCH 純液，以氣味杯內徑調濃度，杯口越大、氣味越濃（該頁圖 5）；標準為 MCH 10 mm、OCT 8 mm（調到沒受訓的果蠅在兩氣味間五五分，也就是訓練前不偏好任何一邊） | 約 150 隻 | 中央小室 90 s → 選擇 120 s；22 °C、相對濕度 50%、暗紅光 | 學習指數 Λ＝躲 CS+ 比例 − 躲 CS− 比例；正值＝躲 CS+ |
| Tomchik 2009 | 電擊；氣味與電擊各 60 s（引 [[s-tully-1985-classical-conditioning]]）；電壓未在該篇正文寫出 | 3-octanol／benzaldehyde | ？待查 | 訓練後 3 分鐘 | P.I.：0＝一半一半，1＝全部選對 |
| Ichinose 2015 | 乾燥蔗糖紙；兩氣味各 1 min | 3-OCT 1%、4-MCH 2%（石蠟油稀釋） | 約 50 隻 | 2 分鐘，取後 60 s；5 min（STM）或 24 h（LTM） | 學習指數 LI，偏好指數公式未寫 |
| Felsenberg 2017 | 乾蔗糖；CS− 2 min → 空氣 30 s → CS+ 2 min | OCT、MCH（礦物油稀釋） | 50–100 隻 | 2 分鐘；訓練後 6 h（部分 3 h、24 h） | PI，公式只引 Krashes & Waddell 2008 |
| Felsenberg 2018 | 90 V 電擊 12 下、每 5 s；CS+ 1 min → 空氣 45 s → CS− 1 min | MCH、OCT（礦物油稀釋 10⁻⁴ 或 10⁻⁶） | 約 80–100 隻 | 2 分鐘；訓練後 60 min | P.I.＝（CS+ 臂數 − CS− 臂數）÷ 總數（引 Tully & Quinn 1985）；躲 CS+ 為負 |

與 Tully 1985 的差別一眼可見：Felsenberg 2018 只在計分公式引用本篇，電壓（90 V 對 60 V）、兩氣味之間的空白（45 s 對 30 s）、隻數（80–100 對約 150）、氣味給法（稀釋液對純液）都不同；Ichinose 2015 與 Felsenberg 2017 是糖獎賞版，CS− 先給的排法（Felsenberg 2017）也與本篇相反。排法本身會影響分數：Tully 1985 圖 6 的電擊訓練中，把標準的「CS+ 在前」改成「CS+ 在後」，Λ 低 7%（※ 從圖判讀約 0.86 → 0.79；差異達統計顯著，P < 0.05）；糖獎賞是否同樣如此，庫內沒有資料。

參數見 [[numbers]]。

## 庫內誰用了它

| 來源 | 用來量什麼 | 得到什麼 |
|---|---|---|
| [[s-tully-1985-classical-conditioning]] | 建立協定時逐一改變參數：訓練循環數、每循環電擊下數、電壓、氣味濃度、CS+ 先或後、時序（逆向／同時／trace 0–45 s）、非聯結對照、消退、逆轉訓練、保留 0–24 h、品系與突變株 | 1 循環 Λ 0.89 ± 0.01，2–5 循環不再上升；1 下 ≈ 0.29、10–12 下 ≈ 0.92；60 V ≈ 0.92 最高；時序 逆向 ≈ −0.03、同時 ≈ 0.79、trace 0／15／30／45 s ≈ 0.47／0.22／0.05／0.00；非聯結對照 ≈ −0.02 至 +0.03；野生型 24 h ≈ 0.15；C-S 0.90、Berlin 0.52（判讀值見 [[numbers]]） |
| [[s-tomchik-2009-camp-dynamics]] | 痕跡制約（氣味結束後空白一段才電擊）的行為時間窗 | 同時給約 0.72，trace 0／15／30／45 s 約 0.47／0.22／0.13／0.05，倒序約 0.04（n＝6，圖判讀） |
| [[s-ichinose-2015-reward-recurrent-circuit]] | 以 [[e-shibire-ts]] 在不同時段關掉迴路後的 STM 與 LTM；類化（換成相似氣味測，見 [[c-odor-generalization]]） | 訓練時與訓練後 1 h 內需要 PAM-α1、MBON-α1、α/β KC，只影響 LTM（見 [[c-memory-consolidation]]） |
| [[s-felsenberg-2017-re-evaluation]] | 訓練後再聞 CS+ 或 CS−（不給糖）之後的 6 h 記憶 | 再聞 CS+ → 消退（PI 約 0.3 → 約 0）；再聞 CS− → 再鞏固（見 [[c-memory-extinction]]、[[c-memory-consolidation]]） |
| [[s-felsenberg-2018-memory-extinction]] | 嫌惡記憶在再聞 CS+ 之後的 60 min 記憶 | 消退只消掉約三分之一到一半的躲避（例：約 −0.39 → −0.20，圖判讀） |

Handler 2019 不用 T 迷宮，只在正文把它當成對照，說自己的小室能反覆訓練與測驗；它的裝置與指標見 [[c-performance-index]]。

## 已知的問題

- **正負號約定不一致，跨篇並列前要先對齊。** Tully 1985：Λ 正值＝躲 CS+（全部躲開＝1）。Tomchik 2009：正值＝避開被電的氣味（1＝全部選對）。Felsenberg 2018：（CS+ − CS−）÷ 總數，**躲 CS+ 是負值**。Felsenberg 2017：正值＝偏向 CS+（糖獎賞）。Ichinose 2015：LI 正值＝選配糖的氣味，但換算公式沒寫。五篇中寫出公式的是 Tully 1985 與 Felsenberg 2018，兩式方向相反（Felsenberg 2018 的值約等於 −Λ）；但兩篇的分母是否都含留在中央的果蠅不確定，見 [[c-performance-index]]。
- **公式與上下限未寫的，只能做同篇內的相對比較**（Tomchik、Ichinose、Felsenberg 2017）。
- **氣味互換取平均。** Tully 1985（OCT 為 CS+ 一組、MCH 為 CS+ 一組，兩組平均為一個 N）、Ichinose、Felsenberg 2017／2018 都讓兩種氣味輪流當 CS+，兩組平均成一個 n；Tomchik 的作法：？待查。
- **測驗時點不同**：0–24 小時的保留曲線（Tully 1985）、3 分鐘、5 分鐘、60 分鐘、6 小時、24 小時都有，「記憶強弱」不能跨篇比。
- 每群隻數與 n 的單位，Tomchik 2009 沒寫清楚（見 [[c-performance-index]] 陷阱 3）。

## 相關

- 概念：[[c-performance-index]]、[[c-memory-extinction]]、[[c-memory-consolidation]]、[[c-cs-us-timing]]、[[c-odor-generalization]]
- 工具：[[e-shibire-ts]]、[[e-olfactory-arena]]
- 主題：[[t-timing-rules]]、[[t-memory-updating]]
- 來源：[[s-tully-1985-classical-conditioning]]、[[s-tomchik-2009-camp-dynamics]]、[[s-ichinose-2015-reward-recurrent-circuit]]、[[s-felsenberg-2017-re-evaluation]]、[[s-felsenberg-2018-memory-extinction]]、[[s-handler-2019-dopamine-receptor-timing]]
