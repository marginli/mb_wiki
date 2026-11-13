---
title: 蕈狀體區室（MB compartment）
created: 2026-10-25
updated: 2026-11-13
tags: [concept, active, mb-learning]
confidence: high
---

# 蕈狀體區室（MB compartment）

**Kenyon 細胞（KC）的軸突成束排成幾條「葉」（lobe）；每條葉沿長度再切成一格一格的區室，每一格由特定一型多巴胺神經元（DAN）的軸突與特定一型輸出神經元（MBON）的樹突共同占據。** 一條 KC 軸突依序穿過好幾格，沿途與每格的 MBON 形成突觸；每格的 DAN **主要**調整自己那一格的 KC→MBON 突觸，但有例外（見陷阱 5）。Hige 2015、Aso 2016、Felsenberg 2017、Pribbenow 2022 都引 Aso et al. 2014a（本庫 [[s-aso-2014-mb-architecture]]）：葉上共 15 個區室（γ、α′/β′、α/β 各 5），另有柄遠端核心 pedc 由一型 MBON 與一型 DAN 專屬支配、不計入 15（見陷阱 10）。

**本頁用語**（每頁可單獨查閱，故重複列出）：

- **KC**：Kenyon 細胞（Kenyon cell），蕈狀體（mushroom body，果蠅腦中把氣味和好壞連起來的構造）裡代表氣味的神經元，每種氣味只活化一小群。
- **DAN**：多巴胺神經元（dopaminergic neuron），送出代表懲罰或獎賞的多巴胺。依 Handler 2019 的說法，PAM 群多報告獎賞、PPL（PPL1）群多報告懲罰。
- **MBON**：蕈狀體輸出神經元（MB output neuron），接收 KC 的訊號，推動果蠅靠近或走開。
- **葉、萼部**：KC 的軸突（送出訊號的長枝）成束排成 α、α′、γ 等「葉」（lobe）；KC 的樹突（接收端）聚在「萼部」（calyx）。
- **光**：指光遺傳活化 DAN，即讓 DAN 帶上照紅光就放電的蛋白，用光代替真的懲罰或獎賞（見 [[c-us-substitution]]）。
- **乙醯膽鹼**（acetylcholine）：嗅覺訊號傳給 KC 時用的化學物質；在取出的腦上噴它，等於「假裝聞到氣味」。
- **rut¹、238Y、c739、MB320C 等**：*rut¹* 是 *rutabaga* 基因的一個突變版本；其餘是「驅動品系」代號，即決定外加基因只在哪些細胞表現的果蠅品系。
- **DopR1、DopR2、內質網鈣**：KC 上兩種多巴胺受體。DopR1 接上製造 cAMP 的路徑；DopR2 接上讓內質網（細胞內存鈣的小倉庫）放出鈣的路徑，所以量內質網鈣就是在看 DopR2 路徑有沒有啟動。

## 怎麼算 / 怎麼判定

- **界定**：依 DAN 與 MBON 的解剖投射範圍（[[s-aso-2014-mb-architecture]]）。細胞以所在區室命名，例如 PPL1-γ1pedc（投射到 γ1pedc 的多巴胺神經元）、MBON-α2sc、γ4 MBON。該篇把 21 型 MBON 的樹突與 20 型 DAN 的末梢分別對位到同一個標準腦，看它們如何鋪排，並以雙色標記與 MCFO 檢驗相鄰區室的界線。
- **區室之下還有一層**：每個區室再依「哪幾型 KC 的軸突經過那一層」細分成**基本分區**（elemental subdivision，Tanaka et al. 2008 稱 synaptic unit），全葉共 37 個（含 pedc）。MBON-α2sc 只取表層與核心層的 KC、MBON-α2p3p 只取後層，差別就在這一層（見陷阱 9）。
- **實驗用法**：用 [[e-split-gal4]] 等驅動品系只活化某一格的 DAN，再記錄同一格或鄰格的 MBON，看改變會不會越界。

## 庫內的用法

| 來源 | 怎麼用 | 得到什麼 |
|---|---|---|
| [[s-hige-2015-heterosynaptic-plasticity]] | 以區室為單位做兩個方向的「越界」測試，並比較不同區室的誘發門檻 | 活化鄰格 DAN，γ1pedc 不變；在 γ1 誘發突觸減弱，鄰格的 MBON-γ2α′1 不變；α2 區用「1 s 氣味配 4 下光」無效，要「60 s 氣味配 120 下光」才有效 |
| [[s-handler-2019-dopamine-receptor-timing]] | 突觸與分子實驗集中在 γ4（另有 γ2、γ5）；cAMP、內質網鈣、多巴胺在 γ4/γ5 量 | γ4 突觸可雙向改變；cAMP 與內質網鈣在被活化 DAN 支配的區室較強（補充圖 S6D–F，細節 ？待查） |
| [[s-cohn-2015-coordinated-neuromodulation]] | 用只在突觸前末梢發光的鈣感測器（sytGCaMP）逐格看同一條 KC 軸突；以 P2X2＋ATP 只活化某幾格的 DAN 或某一顆 MBON | 活體中同一條 γ KC 軸突在 γ2/γ3 的末梢鈣反應強、γ4/γ5 弱，界線對齊 γ3/γ4；離體時各格大致相同。活化 γ4/γ5 DAN 讓 γ4 MBON 增強約三倍（約 0.7 → 2.5 ΔF/F0），γ2 MBON 不顯著；**活化 γ2 DAN 卻讓 γ4 MBON 小幅顯著下降**（約 1.4 → 1.1，約 −20%）；活化任一 γ MBON 都改變各格 DAN |
| [[s-aso-2016-dan-cell-type-rules]] | 以六組驅動品系各自只活化一或兩型 DAN，比較各區室寫入與更新記憶的規則（純行為） | 學習速率、保留時間、被未配對刺激削弱的程度、能否新舊並存，都因區室而異；例如 γ1pedc 學得快、忘得快，α1 不被未配對 DAN 削弱 |
| [[s-ichinose-2015-reward-recurrent-circuit]] | 以 α1 一格為單位：同格的 PAM-α1（DAN）、MBON-α1 與 α/β KC | MBON-α1 末梢緊貼 PAM-α1 樹突，三者在訓練與訓練後 1 小時內都是 24 小時記憶所需（見 [[t-mbon-dan-feedback]]） |
| [[s-felsenberg-2017-re-evaluation]] | 阻斷某一格或某一群的 MBON／DAN，看記憶被重新評估時需要哪幾格 | 再鞏固用同一格的 γ2α′1 MBON 與 PPL1-γ2α′1；消退用 α/α′ 葉的 V2 群 MBON 與鄰格的 PPL1 群 |
| [[s-felsenberg-2018-memory-extinction]] | 比較同一氣味在不同格留下的痕跡 | 消退後，γ1pedc 格（MVP2）的舊嫌惡痕跡仍在，γ5 格（M6 樹突）新出現獎賞型痕跡；兩者在 M6 的輸出端相抵 |
| [[s-tomchik-2009-camp-dynamics]] | **不是區室層級。** 比較的是萼部（calyx，KC 樹突所在）vs 葉部（KC 軸突），以及 α、α′、γ 等不同葉（不同類 KC 的軸突） | cAMP 協同只在葉部出現；多巴胺在萼部的 cAMP 反應有升有降 |
| [[s-gervasi-2010-pka-dynamics]] | **也不是區室層級。** 比較萼部與 α、β、γ 三條葉的 PKA；藥物浴灌、全腦同時泡到 | 浴灌多巴胺只打開 α 葉的 PKA，章魚胺打開全部；作者自己承認，β、γ 葉可能有感測器看不到的小區域被打開，而真實的多巴胺是由特定神經元送到特定區室，本篇沒有量 |
| [[s-huang-2024-dopamine-memory-dynamics]] | 以區室為單位量五型 PPL1 與六型 MBON 的放電（電壓成像）；模型分 γ1、α2、α3 三個模組，接線依連結體 hemibrain v1.2.1 | 改變的持續時間依區室而異：MBON-γ1pedc>α/β 不到 1 小時（短期），MBON-α3 超過 24 小時（長期）；**區室之間經由回饋相連**——γ1pedc 的 MBON 抑制 α3（與 α′2α2）的 DAN，訓練讓這條抑制減弱，α3 的 DAN 才開始對 CS+ 放電。模型的可塑性時間常數 γ 約 30 分鐘、α 約 100 分鐘 |
| [[s-aso-2014-mb-architecture]] | **本概念的出處。** 把 21 型 MBON 的樹突與 20 型 DAN 的末梢分別對位到標準腦，看它們如何鋪排；另在同一顆腦裡以雙色標記與 MCFO 檢驗相鄰區室的界線 | 葉上 15 個區室（γ、α′/β′、α/β 各 5）＋ 柄遠端核心 pedc；**12 個受測交界中確認了 11 個**（β1 與 β2 之間因為缺品系沒測），交界處樹突之間有空隙、Bruchpilot 突觸密度較低。13 型 MBON 只進一格、8 型進兩格；20 型 DAN 中 17 型只投射到一格、3 型兩格。**包鞘膠細胞只分隔三條葉，不出現在同一條葉的區室之間** |
| [[s-mao-2009-dopaminergic-neuron-types]] | 本概念的前身之一。以 flip-out 單細胞選殖看 DAN 一端的分段；以 TH-GAL4 群體鈣成像逐段比較 DAN 末梢 | PPL1 約 12 顆、分出五型伸進葉：α 尖端、α′ 尖端、上段、下段連交界、腳跟連柄末端。四段 DAN 對電擊與氣味的偏好不同（電擊：下段連交界約 74% ＞ α 尖端約 48% ＞ α′ 尖端與上段約 6–8% ΔF/F，※ 從圖判讀）。抗 TH 在水平葉也呈分段，γ 葉分得出 γ3、γ4、γ5（圖 4A3，編號是作者自己標的）。**本篇寫的是 zone、sub-area，還沒有用 compartment 一詞** |
| [[s-dylla-2017-trace-conditioning-dan-plasticity]] | 在活果蠅上以鈣成像同時看九個區室（γ1–γ5、β′1、β′2、α1/α′1、junction）的 DAN 與 KC，並把九區的反應組成向量比較空間樣式 | 各區對氣味與電擊的反應比例不同：γ1、γ2 的 DAN 電擊反應大於氣味，β′ 葉相反。配對造成的改變在 DAN 出現於 9 區中的 8 區，在 KC 只出現於 β′1、β′2、junction。該篇說葉共 15 格，另把 junction 與合併的「α1/α′1」也當區室稱呼——**是自訂的分區，不是 Aso 2014a 的 15 格** |
| [[s-aso-2019-nitric-oxide-cotransmitter]] | 以「每格的 DAN 用不用一氧化氮」當作區分區室的新維度；以抗 NOS 染色量化各區室的訊號（n＝12）；再把 NOS 異位表現到本來沒有的格 | γ1 與 γ5 兩格的 NOS 最高（γ1 顯著高於 12 個區室、γ5 高於 8 個）。在本來沒有內生 NOS 的 PPL1-α3 裡表現 NOS，TH 突變果蠅經 3×1 分鐘訓練就形成正價性記憶（約 +0.18）→ **區室的性質至少有一部分由支配它的 DAN 決定，而不是那一格的 KC 軸突**。保留：γ4 的抗體訊號其實第二高，但 PAM-γ4 的 NOS 轉錄本很低，抗體與 RNA 兩套證據在 γ4 上不一致 |
| [[s-aso-2023-upwind-neurons]] | 比較四個獎賞區室（α1、β1β2、γ4、γ5β′2a）的記憶在讀出時叫出什麼動作 | 四組的二選一 PI 都顯著，但只有 α1、β1β2 的記憶引發迎風移動。作者推測 α/β 葉等成蟲專有的輸出路徑專職循風趨性，γ、β′ 葉多源自幼蟲——**這是假說，本篇沒有檢驗** |
| [[s-yamada-2023-second-order-conditioning]] | 以區室為單位比較「誰能當老師、誰是學生」：光活化四組 PAM 分別寫入 α1、γ5/β′2a、β1/β2、γ4，再測它們教出二階記憶的能力；另以多巴胺感測器 DA2m 看活化 SMP108 時各區室收到多少多巴胺 | 只有 α1 的記憶在一天後仍能當老師（γ5/β′2a 只在訓練完 2 分鐘時有效）。活化 SMP108 時 β′2（約 0.8）、γ4（約 0.6）最亮，γ5、β2、β1 較小，**α1 不亮**（N＝8–12，※ 從圖 6B 判讀）。論文說 DAN 與 MBON 在 KC 軸突上形成 **16 個**區室（與 Aso 2014a 的 15 不同，見陷阱 10） |
| [[s-pribbenow-2022-postsynaptic-plasticity]] | 以 CRISPR 內生 GFP 標記量七種成分（α1、α2、α4–α7、Dlg；**α3 次單元未做成標記**）在各區室的相對螢光；RNAi 後以鄰格正規化（γ5 對 γ4、β′2 對 β′1） | 每個次單元的分布都不同，受體組成在各格並不一致：α5 在整個 γ 葉含 γ5 都高、β′2 略低，α2 在 β′2 與 γ5 同樣偏高，兩者在 α′3 也測得到。**正文寫「至少 15 個區室」，但圖 4b 的熱圖橫軸只有 13 格**（γ5、γ4、γ3、γ2、γ1、β′2、β2、β′1、β1、α′1/1、α′2/2、α′3、α3；※ 從圖判讀），論文沒有說明少了哪幾格 |
| [[s-eschbach-2021-learned-innate-valence-integration]] | **幼蟲**的區室系統：萼、柄、側附區、垂直葉、垂直葉上段、內側葉——**與成蟲的 α/β、α′/β′、γ 葉 15 格不是同一套命名**，論文沒有把兩者對應。區室的記憶方向引自 Eschbach 2020 | 正價值（推動靠近）MBON 多半（4/6）住在懲罰記憶的區室，負價值多半（3/5）住在獎賞記憶的區室——與成蟲同一個原則。萼與垂直葉上段各有一對效果相反的 MBON（a1/a2、e1/e2） |

> 數值見 [[numbers]]。

## 引用時的陷阱

1. **Tomchik 2009 的「軸突 vs 樹突」不等於 DAN–MBON 區室。** 它在葉部末端劃一塊範圍量，空間解析度到「葉」為止；摘要說「協同只限於軸突」。它的依據只有一種組合：乙醯膽鹼與多巴胺都噴在萼部、也在萼部量，結果沒有協同。其他組合（例如多巴胺給葉部、在萼部量）沒測，所以只能說「多巴胺給在萼部時，萼部沒有協同」。不要把它引成「區室專一」的證據。
2. **Hige 2015 的陰性結果有替代解釋。** 鄰格不受影響（n＝6–8 隻），也可能是多巴胺的作用有少量擴散、但沒跨過鄰格的誘發門檻；γ2 區自己的門檻（要多少配對才會誘發改變）沒測。α2 與 γ1 用的驅動品系不同（α2 用的 MB099C 標幾型 DAN，Hige 2015 說四型、Aso 2016 說兩型，見 [[syn-contradictions]] 1.4；γ1 用的 MB320C 只標一顆），門檻差異可能部分來自活化強度。
3. **行為是多區室合成的。** Handler 2019 作者自承單一 γ4 的變化不能完全代表行為；PPL 驅動株支配「六個區室」，論文沒列出是哪六個。
4. ⚠️ Handler 2019 方法章節描述 γ2/γ3 與 γ4/γ5 哪一組在葉的近端（proximal）、哪一組在遠端，同一段前後寫法相反（單篇自身不一致）。
5. **「只調整自己那一格」不是絕對的。** Cohn 2015 圖 6E：只活化 γ2 DAN，γ4 MBON 小幅但顯著地下降（方向與本格的增強相反）；圖 3：活化任一格的 γ MBON 都改變每一格的 DAN。Hige 2015 在 γ1pedc 與鄰格之間沒看到越界，但兩篇測的格、協定不同（Cohn 是單獨活化 DAN、Hige 是配對），不構成直接矛盾。較穩妥的說法是「主要調整自己那一格，他格可出現小幅反向效果」。
6. **MBON 的樹突沒變，不等於這一格的輸出沒變。** Felsenberg 2018 中，嫌惡學習後 M6 樹突（γ5 格）的 CS+／CS− 反應沒有差別，軸突卻有：鄰格的 MVP2 經抑制性連結在 M6 樹突根部附近作用。一格的讀數會被別格的 MBON 改寫。
7. **區室的計數方式不一。** Aso 2016 正文說六組品系涵蓋 15 個區室中的 11 個，但圖上把 γ1pedc 畫成 γ1 與 pedc 兩格，數出來是 12 格（單篇自身不一致）。

8. **Huang 2024 模型裡「α2 沒有作用」是擬合結果，不是實驗排除。** MBON-α2sc 與 MBON-α3 到 PPL1-α3 的興奮性回饋擬合出來近乎為 0，兩模組版（只有 γ1 與 α3）的參數也和三模組版無差異；原文承認 α2 的結果與前人報告不一致。圖 1a 畫出來的連線，不等於模型裡有作用的連線。另外它的「短期／長期」區室是以 MBON 放電改變持續多久來分，不是以需要蛋白質合成與否來分（見 [[c-memory-consolidation]]）。

9. **「15」與「37」是兩個層級。** 15 是區室（MBON 樹突鋪出來的格），37 是基本分區（再依 KC 的層細分）。[[s-aso-2014-mb-architecture]] 的圖 12A 矩陣是後者，圖 10G–L 是前者；該來源頁已逐欄數過 37。庫內寫「每格由一型 DAN 與一型 MBON 負責」時，實際上有三種樣式（一對一、一型 MBON 配兩型 DAN、一型 DAN 配三型 MBON），該篇圖 12B–D 各舉一例。

10. **格數在庫內至少有五個數字，來源各不相同。** [[s-aso-2014-mb-architecture]] 的頭條數字是 **15**（不含柄核心），但它的圖 1C 把 pedc 畫成與區室並列的第 16 格、圖 12A 的矩陣也給它一欄、圖 17J 更把「γ1 ＋ pedc」算成「跨葉」的一例（圖 12C 則只算四型跨葉）；[[s-yamada-2023-second-order-conditioning]] 寫 **16**；[[s-aso-2016-dan-cell-type-rules]] 正文寫六組品系涵蓋 15 格中的 11 格、圖 5B 卻數得出 12 格（單篇自身不一致，根源就是 pedc 算不算）；[[s-dylla-2017-trace-conditioning-dan-plasticity]] 說葉共 15 格，但它實際分析的是自訂的**九區**（含 junction 與合併的 α1/α′1）；[[s-pribbenow-2022-postsynaptic-plasticity]] 正文寫「至少 15」，熱圖只量了 **13** 格。引用任何一個數字前，先確認它指的是「Aso 2014a 的 15 格」「含 pedc 的 16」「某篇自己量到的幾格」還是「37 個基本分區」。

11. **幼蟲的區室不是成蟲的區室。** [[s-eschbach-2021-learned-innate-valence-integration]] 用的是幼蟲命名（萼、柄、側附區、垂直葉、垂直葉上段、內側葉）與幼蟲 MBON 編號（a1…q1），論文沒有把兩套系統逐一對應。可以借用的是**原則**（推動靠近的 MBON 多住在懲罰記憶的區室、推動走開的多住在獎賞記憶的區室），不能借用名字。該篇也顯示另一條成蟲通則在幼蟲不成立：成蟲推動走開的 MBON 全是麩胺酸性，幼蟲推動走開的卻有 GABA 性（h1、h2）與乙醯膽鹼性（a2）（※ 依該篇圖 3d 符號推論）。

12. **「區室的性質由誰決定」有兩個方向的證據。** [[s-aso-2019-nitric-oxide-cotransmitter]] 把 NOS 異位表現到 PPL1-α3，那一格就獲得了原本屬於 γ1pedc／γ5 的「無多巴胺時寫入正價性記憶」的性質——支持性質由支配該格的 DAN 帶來。但 [[s-pribbenow-2022-postsynaptic-plasticity]] 顯示突觸後的受體組成也逐格不同（α5、α2 在 γ5、β′2 偏高），所以讀出端本身也不一致。兩者不衝突，但「換掉 DAN 就換掉這一格」的說法只被測過一個方向（加上 NOS），沒有人做過相反的移植。

13. **區室交界處「突觸密度較低」只看過一種染色。** [[s-aso-2014-mb-architecture]] 的依據是 Bruchpilot 染色與樹突之間的空隙，**沒有量 KC 在交界處的突觸**；該篇自己把「是真的有物理屏障，還是只是兩型樹突的邊界」列為未答（該來源頁第六節）。它同時指出包鞘膠細胞只分隔三條葉、不分隔同一條葉的區室——所以「格」不是由膠細胞隔出來的。

## 相關

- 主題：[[t-dopamine-to-plasticity]]、[[t-timing-rules]]、[[t-mbon-dan-feedback]]、[[t-memory-updating]]
- 概念：[[c-kc-mbon-plasticity]]、[[c-camp-signaling]]、[[c-memory-consolidation]]
- 實體：[[e-mushroom-body]]、[[e-kenyon-cell]]、[[e-dopaminergic-neuron]]、[[e-mbon]]、[[e-split-gal4]]、[[e-mb099c]]、[[e-p2x2]]、[[e-gcamp]]、[[e-th-gal4]]、[[e-mcfo]]
- 綜述：[[syn-contradictions]]
- 來源：[[s-aso-2014-mb-architecture]]、[[s-mao-2009-dopaminergic-neuron-types]]、[[s-hige-2015-heterosynaptic-plasticity]]、[[s-handler-2019-dopamine-receptor-timing]]、[[s-tomchik-2009-camp-dynamics]]、[[s-gervasi-2010-pka-dynamics]]、[[s-cohn-2015-coordinated-neuromodulation]]、[[s-aso-2016-dan-cell-type-rules]]、[[s-ichinose-2015-reward-recurrent-circuit]]、[[s-felsenberg-2017-re-evaluation]]、[[s-felsenberg-2018-memory-extinction]]、[[s-huang-2024-dopamine-memory-dynamics]]、[[s-dylla-2017-trace-conditioning-dan-plasticity]]、[[s-aso-2019-nitric-oxide-cotransmitter]]、[[s-aso-2023-upwind-neurons]]、[[s-yamada-2023-second-order-conditioning]]、[[s-pribbenow-2022-postsynaptic-plasticity]]、[[s-eschbach-2021-learned-innate-valence-integration]]
