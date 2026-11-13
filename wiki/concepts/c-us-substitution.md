---
title: 以人工活化取代非制約刺激（US substitution）
created: 2026-10-25
updated: 2026-11-13
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

本庫出現七類做法（前四類是「怎麼讓神經元放電」，後三類是「拿什麼東西來代替」）：

- **藥物施加**：用玻璃微管把多巴胺噴在蕈狀體上，或把整池灌流液換成含藥的（浴灌）。
- **光遺傳（optogenetics）**：讓 DAN 表現紅光活化的陽離子通道 [[e-cschrimson]] 或 ChrimsonR，飼料加視黃醛當輔因子，照紅光就讓 DAN 放電。Tumkaya 2025 改讓 DAN 表現**藍光**活化的 Chr2XXL，把紅光留給 ORN，兩種顏色因此能分別控制兩條路徑。
- **化學遺傳**：讓 DAN 表現 ATP 門控通道 [[e-p2x2]]，滴 ATP 就讓 DAN 放電。
- **熱遺傳**：讓神經元表現溫度敏感的陽離子通道 [[e-dtrpa1]]（dTrpA1），升溫就讓它放電（Ichinose 2015 在 30 °C 活化輸出神經元 MBON-α1；Aso 2014b 以它活化 PPL1-γ1pedc 代替電擊，溫度與時長 PDF 只寫 thermoactivation：？待查；Burke 2012 在 31 °C 活化章魚胺神經元與 PAM 多巴胺神經元）。
- **用上游的感覺神經元代替**：不叫 DAN，改叫送獎懲訊號給 DAN 的感覺神經元——苦味受器 Gr66a（Aso 2019）、糖受器 Gr64f（Aso 2023、Yamada 2023）、幼蟲的疼痛中間神經元 Basin（Eschbach 2021）。它比直接活化 DAN 多一層自然的轉換，可以用來檢查「直接叫 DAN」有沒有造出人工產物。
- **用已經學會的氣味代替**：二階制約。Yamada 2023 先讓 S1 配糖，再用 S1 本身當增強訊號去教新氣味 S2，增強訊號完全來自腦內既有的記憶。
- **連 CS 一起換掉**：Tumkaya 2025 以紅光活化 ORN 代替氣味（見陷阱 6）；Pribbenow 2022 在離體腦中以噴在 MBON 樹突上的乙醯膽鹼代替氣味、以紅光活化 PAM 代替糖，**CS 與 US 同時被取代**，而且連 KC 都被繞過。

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
| [[s-aso-2014-mbon-valence]] | 熱遺傳：[[e-dtrpa1]] 升溫活化 PPL1-γ1pedc（MB438B）代替電擊。**溫度與時長 PDF 只寫 thermoactivation：？待查**；MB438B 依表 2 另弱標 PPL1-α2α′2 | 3 分鐘嫌惡記憶約 −0.53、對照約 0（圖 6G，※ 從圖判讀）。效果量比同篇真電擊的 2 小時記憶還大，但時間點不同，不能比強弱 |
| [[s-burke-2012-octopamine-dopamine-reward]] | 熱遺傳：[[e-dtrpa1]]，31 °C。協定是「氣味 A 2 min ＠23 °C → 移入預熱的新管、氣味 B 2 min ＠31 °C」。被活化的分別是章魚胺神經元（Tdc2-GAL4）、全部約 130 顆 PAM（0273-GAL4）、約 40 顆 PAM（0104-GAL4），以及三個只標部分章魚胺神經元的品系（NP7088、0665、0891） | 章魚胺神經元可取代糖，PI 約 0.25，**飽足果蠅也成立**，但 3 小時測不到；PAM 遠更有效（0104 約 0.48、0273 約 0.78）且在做不出章魚胺的 *Tβh* 突變株中照常；三個章魚胺子集品系都無效（p > 0.05，n ≥ 6）。※ 注意：這個設計裡**溫度與氣味身分完全共變**，靠只帶 GAL4 或只帶 UAS 的對照組分離，不是靠平衡設計 |
| [[s-aso-2019-nitric-oxide-cotransmitter]] | CsChrimson 紅光（627 nm、34.9 µW/mm²，1 分鐘氣味內給 30 下 1 秒光）代替電擊或糖，七組品系；**另以 Gr66a-GAL4 活化苦味感覺神經元**當「較自然」的對照 | 苦味神經元組同樣出現價性反轉（TH 突變背景下學到喜好）→ **價性反轉不是「用光直接叫 DAN」造成的人工產物**。這是本庫第一次有論文用「上游感覺神經元 vs 直接活化 DAN」檢驗取代的效力 |
| [[s-pribbenow-2022-postsynaptic-plasticity]] | 離體腦＋TTX 2 µM：紅光活化 PAM 群（R58E02-LexA>CsChrimson）取代糖，玻璃微管噴 0.1 mM 乙醯膽鹼（15 ms）在 M6 樹突上取代氣味——**CS 與 US 同時被取代，KC 被繞過**；活體 FRAP 則以局部注射多巴胺 10 mM 取代糖 | 配對 5 次後 M6 對乙醯膽鹼的鈣反應增強約 5–6%（n＝18），只給其一無效（n＝13、10）。**方向與活體糖訓練後 M4 的減弱（約 −35%，n＝9）相反**，作者自己只把它當成原理證明。全部在 TTX 或麻醉下進行，與自然訓練的對應未經檢驗 |
| [[s-aso-2023-upwind-neurons]] | CsChrimson 活化單一區室的獎賞 DAN（MB043C＝α1、MB213B＝β1β2、MB312C＝γ4、MB109B＋MB315C＝γ5β′2a）代替糖；另以 Gr64f split-GAL4 活化糖受器神經元；部分實驗改用真糖訓練 | 四組的 PI 都顯著，但只有 α1、β1β2 叫得出迎風移動（見 [[c-performance-index]] 陷阱 11）。**單獨活化 DAN、不給氣味時不引發迎風**（圖 2A），所以迎風是記憶驅動的，不是 DAN 活化本身的效果 |
| [[s-yamada-2023-second-order-conditioning]] | 三層替代：光活化各型 PAM 代替糖（CsChrimson，S1 配光 1 分鐘、重複 3 次）；光活化 Gr64f 糖味覺神經元代替糖；**以已經學會的氣味 S1 代替獎賞**（二階制約） | 光活化 PAM-α1（MB043C）寫下的一階記憶，一天後仍能教出二階記憶（約 0.46）；γ5/β′2a 只在訓練完 2 分鐘時有效。光活化中間神經元 SMP108（不是 DAN）也能當增強訊號寫下記憶，但那份記憶學得快（第一次 10 秒訓練就到最高值的約 0.95）、掉得也快（12 次測驗後只剩約 0.22）（※ 從圖 8C–F 判讀） |
| [[s-eschbach-2021-learned-innate-valence-integration]] | **幼蟲**；CsChrimson 活化腹神經索的疼痛中間神經元 Basin（GMR72F11）當「人工懲罰」，配天生喜歡的乙酸乙酯（629 nm、2.5 µW/mm²，3 分鐘 × 3 輪）。成像中的訓練改用 660 nm 雷射（約 480 µW/mm²）照 Basin 末梢 | 導航指數由不配對組的約 +0.07 翻成配對組的約 −0.09（※ 從圖 1b 判讀，正文寫 +0.1 與 −0.1）。**活化的不是 DAN 也不是 MBON，而是更上游的傷害訊號中間神經元**；轉彎率的方向依賴在配對組翻號後不顯著（見該來源頁 3.1） |

> 參數見 [[numbers]]。

## 引用時的陷阱

1. **人工 US 的時間尺度與真電擊不同，時間窗不能直接搬。** Tomchik 2009 的行為用真電擊 60 s，成像用秒級的藥物噴射；Hige 2015 生理用 1 ms 光脈衝，行為用 500 ms × 12 下；Handler 2019 少數真電擊實驗是 2 次 1 s、70 V，主實驗則是 1 s 光或約 0.6 s 的 ATP。以人工 US 量出的「幾秒內有效」不等於真實懲罰下的時間窗，見 [[c-cs-us-timing]]。
2. **藥物濃度不等於組織內濃度。** Tomchik 2009 依反應調整噴射壓力與位置，各腦的實際劑量不可比；浴灌 10 mM 多巴胺會作用到整顆腦，分不出是直接作用在 KC 還是經由其他細胞。
3. **驅動品系活化的範圍與強度不同。** Hige 2015 比較 α2 與 γ1 兩個區室時，α2 用的品系 MB099C 同時活化多型 DAN（Hige 2015 說四型、Aso 2016 說兩型，見 [[syn-contradictions]] 1.4），γ1 只活化一顆，「要多少配對才誘發改變」的門檻差異，可能部分來自活化強度；Handler 2019 的 PPL 驅動株支配六個區室，論文未列出。
4. **真電擊只做了少量對照。** Handler 2019 的真電擊實驗只量了 γ2 MBON（補充圖 S3E，？待查）；Hige 2015 的類化引自先前以電擊訓練的研究，本篇行為只用光。
5. **被活化的不一定是 DAN。** Ichinose 2015 活化的是輸出神經元 MBON-α1，它代替糖的效果被解讀為經由「MBON-α1 → PAM-α1」回饋；但「活化 MBON-α1 同時阻斷 PAM-α1」的關鍵對照沒有做。
6. **取代 US 之後，下一個問題是取代 CS——而兩者的證據強度不同。** [[s-tumkaya-2025-synthetic-memory-inception]] 以紅光活化 Orco-Gal4 ORN 代替氣味，再與藍光活化的 DAN 同時給，整場訓練沒有任何自然刺激。喜好方向在兩台裝置上都重現（MOT +0.50、WALISAR +0.38），嫌惡方向只在 MOT 成立（−0.33，95% 信賴區間上界 −0.01），換到 WALISAR 就測不到（+0.07）。**引用「全合成記憶做得出來」時要分方向講**，不要把喜好方向的穩健度套到嫌惡方向。另外，該篇用光照半條通道當 CS，光同時是視覺線索；論文以對照組分數小來排除視覺學習，但圖 3E 有一個不帶 Chrimson 的對照達到 −0.37，大於該格實驗組——該對照只能靠視覺分辨兩種閃爍，可見視覺線索在某些條件下並不次要。
7. **人工 US 不是自然刺激。** Aso 2016 作者自承光遺傳活化「不太可能自然發生」；有三組品系一次活化兩型 DAN，因為只活化一型時記憶太弱。另外，六組品系中只有 MB320C、MB099C 有放電資料（引 Hige 2015），其餘品系的活化強度沒有校準。Cohn 2015 的 58E02 驅動標記範圍與其他篇的描述不同（見 [[e-r58e02]] 與 [[syn-contradictions]] 1.5）。

8. **熱遺傳的開關同時是環境的改變。** [[e-dtrpa1]] 與 [[e-shibire-ts]] 都靠升溫，所以溫度既是工具的開關，也改變果蠅的整體狀態。Burke 2012 的活化協定「氣味 A 在 23 °C、氣味 B 在 31 °C」讓**溫度與氣味身分完全共變**，只能靠對照組（同樣經歷溫度變化、但只帶 GAL4 或只帶 UAS）來分離，不是靠平衡設計（該來源頁第五節第 3 點）。光遺傳沒有這個問題，但紅光本身也是視覺線索（陷阱 6）。

9. **取代的效力可以被檢驗，而本批只有一篇做了。** [[s-aso-2019-nitric-oxide-cotransmitter]] 把「光活化 DAN」換成「光活化苦味感覺神經元（Gr66a）」，兩者都出現價性反轉，所以那個現象不是「強迫 DAN 齊發」的人工產物。其餘各篇都沒有做這種上游對照；[[s-aso-2023-upwind-neurons]] 與 [[s-yamada-2023-second-order-conditioning]] 雖然也用 Gr64f 糖受器神經元，但那是另一組實驗，不是用來檢驗 DAN 活化的對照。

10. **「活化某型 DAN」不等於「在那一格給多巴胺」。** [[s-aso-2019-nitric-oxide-cotransmitter]] 在做不出多巴胺的 TH 突變背景下活化 DAN（細胞照常放電、但沒有多巴胺可放），PPL1-γ1pedc 與 PAM-γ5／β′2a 造出的記憶**價性相反**，並指認一氧化氮是這兩型的共同傳遞物；PPL1-γ2α′1 則不反轉。所以人工活化送出去的是「這型 DAN 的全部傳遞物」，不是多巴胺。

11. **被取代的那一側可能不只一邊。** [[s-pribbenow-2022-postsynaptic-plasticity]] 在離體腦中同時換掉 CS（噴乙醯膽鹼）與 US（光活化 PAM），還加 TTX 讓網路安靜、讓 KC 完全不被活化。好處是能單獨檢驗突觸後那一側；代價是 TTX 同時移除了 MBON 之間的去抑制與網路回饋，而且量到的方向（增強約 5–6%）與活體糖訓練後 M4 的減弱（約 −35%）相反，作者自己說這組只應視為原理證明。

12. **增強訊號可以來自腦內。** [[s-yamada-2023-second-order-conditioning]] 的二階制約用「已經學會的 S1」當 US，教學訊號完全來自既有記憶，經「MBON-α1 → SMP353/354 → SMP108 → 學生格的 PAM」這條路轉成多巴胺。這篇也示範了取代的另一個限制：**只有 α1 這一格的記憶在一天後還能當老師**，γ5/β′2a 只在剛訓練完 2 分鐘時有效，所以「哪一格寫的記憶」決定了它能不能再當增強訊號。

## 相關

- 主題：[[t-timing-rules]]、[[t-dopamine-to-plasticity]]、[[t-mbon-dan-feedback]]
- 概念：[[c-cs-us-timing]]、[[c-performance-index]]、[[c-kc-mbon-plasticity]]
- 實體：[[e-cschrimson]]、[[e-p2x2]]、[[e-dopaminergic-neuron]]、[[e-split-gal4]]、[[e-r58e02]]、[[e-mb099c]]、[[e-ppl1-gamma1pedc]]、[[e-shibire-ts]]、[[e-dtrpa1]]、[[e-olfactory-arena]]、[[e-t-maze]]
- 來源：[[s-tomchik-2009-camp-dynamics]]、[[s-hige-2015-heterosynaptic-plasticity]]、[[s-handler-2019-dopamine-receptor-timing]]、[[s-cohn-2015-coordinated-neuromodulation]]、[[s-aso-2016-dan-cell-type-rules]]、[[s-ichinose-2015-reward-recurrent-circuit]]、[[s-tumkaya-2025-synthetic-memory-inception]]、[[s-aso-2014-mbon-valence]]、[[s-burke-2012-octopamine-dopamine-reward]]、[[s-aso-2019-nitric-oxide-cotransmitter]]、[[s-pribbenow-2022-postsynaptic-plasticity]]、[[s-aso-2023-upwind-neurons]]、[[s-yamada-2023-second-order-conditioning]]、[[s-eschbach-2021-learned-innate-valence-integration]]
