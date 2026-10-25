---
title: 蘑菇體區室（MB compartment）
created: 2026-10-25
updated: 2026-10-25
tags: [concept, active, mb-learning]
confidence: high
---

# 蘑菇體區室（MB compartment）

**Kenyon 細胞（KC）的軸突成束排成幾條「葉」（lobe）；每條葉沿長度再切成一格一格的區室，每一格由特定一型多巴胺神經元（DAN）的軸突與特定一型輸出神經元（MBON）的樹突共同占據。** 一條 KC 軸突依序穿過好幾格，沿途與每格的 MBON 形成突觸；每格的 DAN **主要**調整自己那一格的 KC→MBON 突觸，但有例外（見陷阱 5）。Hige 2015、Aso 2016、Felsenberg 2017 都引 Aso et al. 2014a：共 15 個區室。

**本頁用語**（每頁可單獨查閱，故重複列出）：

- **KC**：Kenyon 細胞（Kenyon cell），蘑菇體（mushroom body，果蠅腦中把氣味和好壞連起來的構造）裡代表氣味的神經元，每種氣味只活化一小群。
- **DAN**：多巴胺神經元（dopaminergic neuron），送出代表懲罰或獎賞的多巴胺。依 Handler 2019 的說法，PAM 群多報告獎賞、PPL（PPL1）群多報告懲罰。
- **MBON**：蘑菇體輸出神經元（MB output neuron），接收 KC 的訊號，推動果蠅靠近或走開。
- **葉、萼部**：KC 的軸突（送出訊號的長枝）成束排成 α、α′、γ 等「葉」（lobe）；KC 的樹突（接收端）聚在「萼部」（calyx）。
- **光**：指光遺傳活化 DAN，即讓 DAN 帶上照紅光就放電的蛋白，用光代替真的懲罰或獎賞（見 [[c-us-substitution]]）。
- **乙醯膽鹼**（acetylcholine）：嗅覺訊號傳給 KC 時用的化學物質；在取出的腦上噴它，等於「假裝聞到氣味」。
- **rut¹、238Y、c739、MB320C 等**：*rut¹* 是 *rutabaga* 基因的一個突變版本；其餘是「驅動品系」代號，即決定外加基因只在哪些細胞表現的果蠅品系。
- **DopR1、DopR2、內質網鈣**：KC 上兩種多巴胺受體。DopR1 接上製造 cAMP 的路徑；DopR2 接上讓內質網（細胞內存鈣的小倉庫）放出鈣的路徑，所以量內質網鈣就是在看 DopR2 路徑有沒有啟動。

## 怎麼算 / 怎麼判定

- **界定**：依 DAN 與 MBON 的解剖投射範圍（Aso et al. 2014a）。細胞以所在區室命名，例如 PPL1-γ1pedc（投射到 γ1pedc 的多巴胺神經元）、MBON-α2sc、γ4 MBON。
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

> 數值見 [[numbers]]。

## 引用時的陷阱

1. **Tomchik 2009 的「軸突 vs 樹突」不等於 DAN–MBON 區室。** 它在葉部末端劃一塊範圍量，空間解析度到「葉」為止；摘要說「協同只限於軸突」。它的依據只有一種組合：乙醯膽鹼與多巴胺都噴在萼部、也在萼部量，結果沒有協同。其他組合（例如多巴胺給葉部、在萼部量）沒測，所以只能說「多巴胺給在萼部時，萼部沒有協同」。不要把它引成「區室專一」的證據。
2. **Hige 2015 的陰性結果有替代解釋。** 鄰格不受影響（n＝6–8 隻），也可能是多巴胺的作用有少量擴散、但沒跨過鄰格的誘發門檻；γ2 區自己的門檻（要多少配對才會誘發改變）沒測。α2 與 γ1 用的驅動品系不同（α2 用的 MB099C 標幾型 DAN，Hige 2015 說四型、Aso 2016 說兩型，見 [[syn-contradictions]] 1.4；γ1 用的 MB320C 只標一顆），門檻差異可能部分來自活化強度。
3. **行為是多區室合成的。** Handler 2019 作者自承單一 γ4 的變化不能完全代表行為；PPL 驅動株支配「六個區室」，論文沒列出是哪六個。
4. ⚠️ Handler 2019 方法章節描述 γ2/γ3 與 γ4/γ5 哪一組在葉的近端（proximal）、哪一組在遠端，同一段前後寫法相反（單篇自身不一致）。
5. **「只調整自己那一格」不是絕對的。** Cohn 2015 圖 6E：只活化 γ2 DAN，γ4 MBON 小幅但顯著地下降（方向與本格的增強相反）；圖 3：活化任一格的 γ MBON 都改變每一格的 DAN。Hige 2015 在 γ1pedc 與鄰格之間沒看到越界，但兩篇測的格、協定不同（Cohn 是單獨活化 DAN、Hige 是配對），不構成直接矛盾。較穩妥的說法是「主要調整自己那一格，他格可出現小幅反向效果」。
6. **MBON 的樹突沒變，不等於這一格的輸出沒變。** Felsenberg 2018 中，嫌惡學習後 M6 樹突（γ5 格）的 CS+／CS− 反應沒有差別，軸突卻有：鄰格的 MVP2 經抑制性連結在 M6 樹突根部附近作用。一格的讀數會被別格的 MBON 改寫。
7. **區室的計數方式不一。** Aso 2016 正文說六組品系涵蓋 15 個區室中的 11 個，但圖上把 γ1pedc 畫成 γ1 與 pedc 兩格，數出來是 12 格（單篇自身不一致）。

## 相關

- 主題：[[t-dopamine-to-plasticity]]、[[t-timing-rules]]、[[t-mbon-dan-feedback]]、[[t-memory-updating]]
- 概念：[[c-kc-mbon-plasticity]]、[[c-camp-signaling]]
- 實體：[[e-mushroom-body]]、[[e-kenyon-cell]]、[[e-dopaminergic-neuron]]、[[e-mbon]]、[[e-split-gal4]]、[[e-mb099c]]、[[e-p2x2]]
- 綜述：[[syn-contradictions]]
- 來源：[[s-hige-2015-heterosynaptic-plasticity]]、[[s-handler-2019-dopamine-receptor-timing]]、[[s-tomchik-2009-camp-dynamics]]、[[s-cohn-2015-coordinated-neuromodulation]]、[[s-aso-2016-dan-cell-type-rules]]、[[s-ichinose-2015-reward-recurrent-circuit]]、[[s-felsenberg-2017-re-evaluation]]、[[s-felsenberg-2018-memory-extinction]]
