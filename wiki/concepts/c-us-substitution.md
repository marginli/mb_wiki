---
title: 以人工活化取代非制約刺激（US substitution）
created: 2026-10-25
updated: 2026-11-12
tags: [concept, active, mb-learning]
confidence: high
---

# 以人工活化取代非制約刺激（US substitution）

**不給真正的電擊或糖，改用人為方法直接活化傳遞「懲罰／獎賞」的多巴胺神經元（DAN），或直接施加多巴胺，當作非制約刺激（unconditioned stimulus, US）。** 好處是能精準控制 US 的時點、長短，以及到底是哪一群神經元送出訊號。

**本頁用語**（每頁可單獨查閱，故重複列出）：

- **KC**：Kenyon 細胞（Kenyon cell），蕈狀體（mushroom body，果蠅腦中把氣味和好壞連起來的構造）裡代表氣味的神經元，每種氣味只活化一小群。
- **DAN**：多巴胺神經元（dopaminergic neuron），送出代表懲罰或獎賞的多巴胺。依 Handler 2019 的說法，PAM 群多報告獎賞、PPL（PPL1）群多報告懲罰。
- **MBON**：蕈狀體輸出神經元（MB output neuron），接收 KC 的訊號，推動果蠅靠近或走開。
- **葉、萼部**：KC 的軸突（送出訊號的長枝）成束排成 α、α′、γ 等「葉」（lobe）；KC 的樹突（接收端）聚在「萼部」（calyx）。
- **區室**：葉沿長度切成的一格，以 γ1pedc、γ2、γ4、α2 等編號命名；細胞也以所在區室命名，例如 MBON-γ1pedc、PPL1-γ1pedc。詳見 [[c-mb-compartment]]。
- **章魚胺**（octopamine）：昆蟲腦中類似腎上腺素的物質，Tomchik 2009 當時被認為傳遞獎賞，所以拿來和多巴胺對照。
- **離體、在體、閉迴路**：離體＝取出的腦泡在養液裡；在體＝活果蠅頭部固定、打開腦殼；閉迴路＝頭部固定的果蠅踩在球上走，送氣管隨牠的轉向轉動，可同時記錄行為與腦。
- **rut¹、238Y、c739、MB320C 等**：*rut¹* 是 *rutabaga* 基因的一個突變版本；其餘是「驅動品系」代號，即決定外加基因只在哪些細胞表現的果蠅品系。

## 怎麼算 / 怎麼判定

本庫出現四類做法：

- **藥物施加**：用玻璃微管把多巴胺噴在蕈狀體上，或把整池灌流液換成含藥的（浴灌）。
- **光遺傳（optogenetics）**：讓 DAN 表現紅光活化的陽離子通道 [[e-cschrimson]] 或 ChrimsonR，飼料加視黃醛當輔因子，照紅光就讓 DAN 放電。Tumkaya 2025 改讓 DAN 表現**藍光**活化的 Chr2XXL，把紅光留給 ORN，兩種顏色因此能分別控制兩條路徑。
- **化學遺傳**：讓 DAN 表現 ATP 門控通道 [[e-p2x2]]，滴 ATP 就讓 DAN 放電。
- **熱遺傳**：讓神經元表現溫度敏感的陽離子通道 dTrpA1，升到 30 °C 就讓它放電（Ichinose 2015；被活化的是輸出神經元，不是 DAN）。

## 庫內的用法

| 來源 | 怎麼用 | 得到什麼 |
|---|---|---|
| [[s-tomchik-2009-camp-dynamics]] | 離體腦：多巴胺 1 mM（模擬懲罰）或章魚胺 100 µM 噴在垂直葉（α、α′ 葉）；另以浴灌 30 s 做劑量反應。噴射時長 ？待查（補充資料未取得） | KC 軸突 cAMP 的協同與時間窗 |
| [[s-hige-2015-heterosynaptic-plasticity]] | CsChrimson 只表現在一顆 PPL1-γ1pedc（品系 MB320C）；627 nm，1 ms × 4 下（2 Hz），另有 1 下與 120 下的協定；行為訓練用 500 ms × 12 下 | MBON-γ1pedc 的突觸減弱；行為學習與類化（學會迴避一種氣味後，也迴避相似氣味） |
| [[s-handler-2019-dopamine-receptor-timing]] | 行為：CsChrimson，627 nm 照 1 s（PAM 群 MB042B、PPL 群 MB504B）；閉迴路：ChrimsonR，565 nm 照 1 s；離體：P2X2＋2 mM ATP，5 × 100 ms（約 0.6 s） | 時序決定學習方向；γ4 突觸雙向改變 |
| [[s-cohn-2015-coordinated-neuromodulation]] | 離體與活體：P2X2＋ATP（管內 2 mM）活化 58E02 標記的 γ4/γ5 DAN（γ3 標記不穩定）或 γ2 DAN；噴注時長與壓力主文未寫（？待查）。自然刺激只有吃糖（0.2–1 M 蔗糖）與腹部電擊（0.5 s、60–150 V），電擊只用於 DAN 成像 | 不搭配 KC 刺激、單獨活化 DAN，本格 KC→MBON 突觸變強；與 KC 刺激相隔 ＜ 500 ms 則減弱。無行為讀數 |
| [[s-aso-2016-dan-cell-type-rules]] | 行為：CsChrimson（20xUAS-CsChrimson-mVenus）由六組驅動品系表現，627 nm、34.9 µW/mm²；標準訓練 60 s 氣味內 30 下、每下 1 s；ISI 掃描用 10 s 氣味配 3 下 | 各區室寫入與更新記憶的規則不同；同一顆 PPL1-γ1pedc 依時序寫入嫌惡或喜好；只給光不給氣味會削弱已有記憶 |
| [[s-ichinose-2015-reward-recurrent-circuit]] | 不給糖，以 dTrpA1 在 30 °C 活化輸出神經元 MBON-α1（品系 MB310C）1 分鐘配氣味 | 誘發 24 小時獎賞記憶，學習指數約 0.15（兩個對照約 −0.05 與 0.00）；真糖訓練的對照多在 0.3–0.45 |
| [[s-tumkaya-2025-synthetic-memory-inception]] | Chr2XXL（藍光，峰值 460 nm）表現在 TH-LexA（含 PPL1 的 TH⁺ 子集，嫌惡）或 R58E02-LexA（PAM，獎賞）。嫌惡 12 次脈衝；**獎賞只在 60 s 訓練期最初 3 秒給 1 次**，因 Chr2XXL 關閉慢 | 配真氣味時：TH 半 ΔPI −0.44、PAM 半 +0.64。本篇進一步在**行為實驗中**把 CS 也換成光（見陷阱 6）；[[s-tomchik-2009-camp-dynamics]] 在離體腦上以乙醯膽鹼代替氣味、多巴胺代替懲罰，也同時換掉兩邊，但沒有行為讀數 |

> 參數見 [[numbers]]。

## 引用時的陷阱

1. **人工 US 的時間尺度與真電擊不同，時間窗不能直接搬。** Tomchik 2009 的行為用真電擊 60 s，成像用秒級的藥物噴射；Hige 2015 生理用 1 ms 光脈衝，行為用 500 ms × 12 下；Handler 2019 少數真電擊實驗是 2 次 1 s、70 V，主實驗則是 1 s 光或約 0.6 s 的 ATP。以人工 US 量出的「幾秒內有效」不等於真實懲罰下的時間窗，見 [[c-cs-us-timing]]。
2. **藥物濃度不等於組織內濃度。** Tomchik 2009 依反應調整噴射壓力與位置，各腦的實際劑量不可比；浴灌 10 mM 多巴胺會作用到整顆腦，分不出是直接作用在 KC 還是經由其他細胞。
3. **驅動品系活化的範圍與強度不同。** Hige 2015 比較 α2 與 γ1 兩個區室時，α2 用的品系 MB099C 同時活化多型 DAN（Hige 2015 說四型、Aso 2016 說兩型，見 [[syn-contradictions]] 1.4），γ1 只活化一顆，「要多少配對才誘發改變」的門檻差異，可能部分來自活化強度；Handler 2019 的 PPL 驅動株支配六個區室，論文未列出。
4. **真電擊只做了少量對照。** Handler 2019 的真電擊實驗只量了 γ2 MBON（補充圖 S3E，？待查）；Hige 2015 的類化引自先前以電擊訓練的研究，本篇行為只用光。
5. **被活化的不一定是 DAN。** Ichinose 2015 活化的是輸出神經元 MBON-α1，它代替糖的效果被解讀為經由「MBON-α1 → PAM-α1」回饋；但「活化 MBON-α1 同時阻斷 PAM-α1」的關鍵對照沒有做。
6. **取代 US 之後，下一個問題是取代 CS——而兩者的證據強度不同。** [[s-tumkaya-2025-synthetic-memory-inception]] 以紅光活化 Orco-Gal4 ORN 代替氣味，再與藍光活化的 DAN 同時給，整場訓練沒有任何自然刺激。喜好方向在兩台裝置上都重現（MOT +0.50、WALISAR +0.38），嫌惡方向只在 MOT 成立（−0.33，95% 信賴區間上界 −0.01），換到 WALISAR 就測不到（+0.07）。**引用「全合成記憶做得出來」時要分方向講**，不要把喜好方向的穩健度套到嫌惡方向。另外，該篇用光照半條通道當 CS，光同時是視覺線索；論文以對照組分數小來排除視覺學習，但圖 3E 有一個不帶 Chrimson 的對照達到 −0.37，大於該格實驗組——該對照只能靠視覺分辨兩種閃爍，可見視覺線索在某些條件下並不次要。
7. **人工 US 不是自然刺激。** Aso 2016 作者自承光遺傳活化「不太可能自然發生」；有三組品系一次活化兩型 DAN，因為只活化一型時記憶太弱。另外，六組品系中只有 MB320C、MB099C 有放電資料（引 Hige 2015），其餘品系的活化強度沒有校準。Cohn 2015 的 58E02 驅動標記範圍與其他篇的描述不同（見 [[e-r58e02]] 與 [[syn-contradictions]] 1.5）。

## 相關

- 主題：[[t-timing-rules]]、[[t-dopamine-to-plasticity]]、[[t-mbon-dan-feedback]]
- 概念：[[c-cs-us-timing]]、[[c-performance-index]]、[[c-kc-mbon-plasticity]]
- 實體：[[e-cschrimson]]、[[e-p2x2]]、[[e-dopaminergic-neuron]]、[[e-split-gal4]]、[[e-r58e02]]、[[e-mb099c]]、[[e-ppl1-gamma1pedc]]
- 來源：[[s-tomchik-2009-camp-dynamics]]、[[s-hige-2015-heterosynaptic-plasticity]]、[[s-handler-2019-dopamine-receptor-timing]]、[[s-cohn-2015-coordinated-neuromodulation]]、[[s-aso-2016-dan-cell-type-rules]]、[[s-ichinose-2015-reward-recurrent-circuit]]、[[s-tumkaya-2025-synthetic-memory-inception]]
