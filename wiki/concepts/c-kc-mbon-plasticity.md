---
title: KC→MBON 突觸可塑性（KC-MBON synaptic plasticity）
created: 2026-10-25
updated: 2026-11-13
tags: [concept, active, mb-learning]
confidence: medium
---

# KC→MBON 突觸可塑性（KC-MBON synaptic plasticity）

**Kenyon 細胞（KC）把氣味訊號經突觸交給蕈狀體輸出神經元（MBON），MBON 再推動果蠅「靠近」或「走開」；這個突觸的強度被多巴胺改變，就是 KC→MBON 突觸可塑性。** 變弱並持續稱長期抑制（long-term depression, LTD），變強稱增強（potentiation）。由第三個神經元（這裡是多巴胺神經元 DAN）改變另外兩者之間突觸的現象，稱**異突觸可塑性（heterosynaptic plasticity）**；只由突觸兩端自身活動決定的，稱同突觸（homosynaptic）可塑性。

**本頁用語**（每頁可單獨查閱，故重複列出）：

- **KC**：Kenyon 細胞（Kenyon cell），蕈狀體（mushroom body，果蠅腦中把氣味和好壞連起來的構造）裡代表氣味的神經元，每種氣味只活化一小群。
- **DAN**：多巴胺神經元（dopaminergic neuron），送出代表懲罰或獎賞的多巴胺。依 Handler 2019 的說法，PAM 群多報告獎賞、PPL（PPL1）群多報告懲罰。
- **MBON**：蕈狀體輸出神經元（MB output neuron），接收 KC 的訊號，推動果蠅靠近或走開。
- **葉、萼部**：KC 的軸突（送出訊號的長枝）成束排成 α、α′、γ 等「葉」（lobe）；KC 的樹突（接收端）聚在「萼部」（calyx）。
- **區室**：葉沿長度切成的一格，以 γ1pedc、γ2、γ4、α2 等編號命名；細胞也以所在區室命名，例如 MBON-γ1pedc、PPL1-γ1pedc。詳見 [[c-mb-compartment]]。
- **光**：指光遺傳活化 DAN，即讓 DAN 帶上照紅光就放電的蛋白，用光代替真的懲罰或獎賞（見 [[c-us-substitution]]）。
- **forskolin**：直接活化製造 cAMP 的酵素的藥，用來人為拉高 cAMP。
- **ΔR/R、ΔF/F**：螢光感測器的訊號（兩色亮度比值，或亮度）相對刺激前基線的變化比例，例如 0.15＝高了 15%。只能在同一實驗內比大小。
- **離體、在體、閉迴路**：離體＝取出的腦泡在養液裡；在體＝活果蠅頭部固定、打開腦殼；閉迴路＝頭部固定的果蠅踩在球上走，送氣管隨牠的轉向轉動，可同時記錄行為與腦。
- **CS+／CS−**：訓練時配了糖或電擊的氣味／沒配的對照氣味。
- **電壓成像、anti-Hebbian**：電壓成像＝用會隨膜電壓變亮的螢光蛋白看每一次放電（Huang 2024）；anti-Hebbian 規則＝KC 放電時，同格 DAN 放電增加則 KC→MBON 變弱、DAN 被抑制則變強（Huang 2024 模型的假設）。
- **−/−**：該基因兩份都被剔除。
- **DopR1、DopR2、內質網鈣**：KC 上兩種多巴胺受體。DopR1 接上製造 cAMP 的路徑；DopR2 接上讓內質網（細胞內存鈣的小倉庫）放出鈣的路徑，所以量內質網鈣就是在看 DopR2 路徑有沒有啟動。

## 怎麼算 / 怎麼判定

配對前後各量一次「同樣的 KC 輸入讓 MBON 反應多少」，相減或算比例：

- Hige 2015：活體全細胞記錄（把玻璃電極接上單一神經元、直接量它的電訊號）MBON，量氣味開始後 0–1.4 s 的放電次數，以及突觸電流的總電荷（電荷轉移，pC）。
- Handler 2019：離體腦以乙醯膽鹼刺激 KC，量 γ4 MBON 的鈣反應（用會隨鈣變亮的螢光蛋白 GCaMP6s 量，代表 MBON 被 KC 驅動的程度）的峰值 ΔF/F；在體則量 γ4 對氣味的反應。

## 庫內的用法

| 來源 | 怎麼用 | 得到什麼 |
|---|---|---|
| [[s-hige-2015-heterosynaptic-plasticity]] | 氣味配一顆 DAN 的光活化，直接量突觸 | **單向減弱**：MBON-γ1pedc 配對氣味放電降 80% ± 5.7%、電荷降 90% ± 3.7%，至少 40 分鐘；MBON 不放電也會發生（表示由 KC 與 DAN 決定，不需突觸後的活動）；逆向配對無效 |
| [[s-handler-2019-dopamine-receptor-timing]] | 不同時間差配對；剔除受體 | **雙向**：γ4 MBON 對 KC 刺激的峰值反應（ΔF/F）逆向（−1.2 s）配對前約 1.22 → 配對後 2.8，增強；順向（+0.5 s）配對前約 1.22 → 配對後 0.42，減弱；DopR1 剔除後不再減弱，DopR2 剔除後不再增強 |
| [[s-cohn-2015-coordinated-neuromodulation]] | 離體：P2X2＋ATP 活化 γ4/γ5 DAN，膜片鉗或鈣影像量 γ4 MBON；配對（＜ 500 ms）與不配對（＞ 45 s）輪流做 | **不配對也會改變，而且是變強**：γ4 MBON 的 EPSC 約 1.5 → 16 pA，ΔF/F0 約 0.7 → 2.5；配對讓已被增強的反應壓回（約 2.0 → 0.35）；活體雙氣味實驗中，配對氣味相對未配對氣味的比值約 1.35 → 0.6 |
| [[s-felsenberg-2017-re-evaluation]] | 糖獎賞訓練後 3 小時，活體量 γ2α′1 MBON 對 CS+、CS− 的鈣反應 | **沒配糖的 CS− 反應變大**（標準化 AUC 約 +14% 與 +24%），CS+ 不變；V2 群 MBON 不變 |
| [[s-felsenberg-2018-memory-extinction]] | 電擊訓練或訓練後再消退，活體量 MVP2、M4β′、M6 的樹突與軸突 | MVP2 樹突 CS+ ＜ CS−（嫌惡痕跡），消退後仍在；M6 樹突在消退後新出現 CS+ ＜ CS−；只訓練時 M6 軸突 CS+ 較大、樹突沒有 |
| [[s-tomchik-2009-camp-dynamics]] | **沒量 KC→MBON 突觸。** 量的是 KC 軸突本身的鈣反應在 cAMP 拉高後是否變大 | forskolin 使 α 葉鈣反應約 3.2 倍、多巴胺約 2 倍；作者稱「突觸前可塑性」，討論中稱其為異突觸 |
| [[s-minnick-2026-untrained-connectome]] | **不是實驗，是模擬**：讓嫌惡區室的 8,377 條 KC→MBON 連結在增強訊號下依適任痕跡變弱，其餘 7,146 條不動 | 平均權重 0.513 → 0.138 mV；推動趨近的 MBON 由每步 103 個脈衝降到 37、推動躲避的維持 50，價性由 +1.41 轉為 −0.33，行為由趨近轉為躲避。**但在原樣讀出的網路中，不給氣味也一樣會減弱**（見 [[c-sparse-coding]] 陷阱 2） |
| [[s-huang-2024-dopamine-memory-dynamics]] | 活體電壓成像量 MBON 對 CS+、CS− 的放電改變（不是直接量突觸）；九神經元模型以**雙向 anti-Hebbian 規則**更新 KC→MBON 權重，參數擬合 86 個放電率 | 實測：電擊訓練後 MBON-γ1pedc>α/β、γ2α′1 對 CS+ 下降、約 1 小時恢復；MBON-α3 下降持續 24 小時以上。模型：γ 區室可塑性時間常數約 30 分鐘、α 區室約 100 分鐘；吸引氣味的 CS− 讓 DAN 安靜，依規則 KC2→MBON 變強。**雙向規則是模型假設，不是量測** |
| [[s-pribbenow-2022-postsynaptic-plasticity]] | **本庫唯一直接操作突觸後那一側的分子**：離體腦＋TTX 繞過 KC，乙醯膽鹼 0.1 mM 噴 M6 樹突、同時紅光活化 PAM（R58E02-LexA）；另在活體以絕對式糖訓練量 M4 軸突；再以 RNAi 在 M4/6 逐一降低 nAChR 的七個 α 次單元與支架蛋白 Dlg | 離體配對 5 次後 M6 對乙醯膽鹼的鈣反應**增強**，後測／前測約 1.05–1.06（n＝18，比值成對 t 檢定，p<0.05），只給乙醯膽鹼（n＝13）或只給光（n＝10）無效。活體糖訓練後 M4 對受訓氣味**減弱**（後測約為前測的 0.65，n＝9），不配對組不變。獎賞記憶需要 M4/6 上的 α5（立即）與 α1／α2／Dlg（3 小時），嫌惡記憶幾乎都不需要。**兩個方向相反，作者自己把離體那組定位為原理證明** |
| [[s-dylla-2017-trace-conditioning-dan-plasticity]] | **沒有量 MBON。** 以 GCaMP3 量 KC 軸突在九個區室的鈣反應（活體、痕跡制約，氣味結束後空白 5 秒才電擊），比較配對組與不配對組 | 配對組相對不配對組，KC 對 CS 的反應在 β′1（`*`）、β′2（`**`）、junction（`*`）較小，第 10 回合差值 −0.09、−0.10、−0.17（正規化值）；γ 葉各格不顯著（γ1 差值也是 −0.17，但 p＝0.068、配對組只有 9 隻）。量的位置正是 KC 軸突與 MBON 接觸之處，作者據此推論 KC→MBON 的**突觸前**減弱——這是從位置推來的，不是突觸量測 |
| [[s-yamada-2023-second-order-conditioning]] | 二階制約時在活體全細胞記錄 MBON-γ5β′2a 的次閾值反應（取氣味開始後 0–20.6 秒的平均去極化） | **跨區室誘發的減弱**：對 S2+ 的反應由第 1 回合約 5.1 mV 降到第 2–5 回合約 2.4–3.6 mV，對 S2− 五回合都沒有顯著差別（二因子 ANOVA p＝0.003，n＝14）。**峰值振幅不變（p＝0.87）**，改變的是氣味持續期間的平台，與本庫其他以峰值報告的研究不是同一個量。二階制約期間的增強訊號來自腦內（SMP108 → 學生格的 PAM），不是外來的糖 |
| [[s-aso-2019-nitric-oxide-cotransmitter]] | **沒有量突觸。** 以行為 PI 反推，並以一個雙路徑模型描述：多巴胺造成抑制、一氧化氮造成增強 | 模型取 w ∝ (1 − D)(1 + N)（相乘）而非 w ∝ N − D（相加），因為相加模型預測重複配對後記憶反而變弱、與資料不符；時間常數 τ_D ＝ 30 秒、τ_N ＝ 10 分鐘，速率 A_DA ＝ 4.3 min⁻¹、A_NO ＝ 0.96 min⁻¹。**「一氧化氮使突觸增強」是模型假設**，作者自承需要生理實驗檢驗（可直接接上 Hige 2015 在 γ1pedc 的作法） |
| [[s-aso-2014-mbon-valence]] | **沒有量突觸**，也沒有量任何 MBON 對氣味的反應；由「活化某型 MBON 的行為方向」與「同格 DAN 寫入的記憶方向」相反推論 | 作者寫「多巴胺壓低該格 KC→MBON 的突觸傳遞」是**最容易解釋**的假設（圖 14 圖說），並另列兩種替代機制。本篇常被引為「突觸變弱」的依據，但它是推論；直接量測是 [[s-hige-2015-heterosynaptic-plasticity]] |

> 數值見 [[numbers]]；γ4 與 Tomchik 的倍數為從圖判讀。

**[[s-eschbach-2021-learned-innate-valence-integration]] 沒有列進上表。** 它是幼蟲研究，嫌惡訓練後量到 MBON-m1 對 CS+ 的鈣反應降到約三成（9 隻），但量的是**整顆 MBON 對氣味的反應**，不是 KC→MBON 突觸；作者自己列了兩條可能路徑——(i) KC 與 DAN 同時活化直接壓低 KC→MBON-m1，(ii) 別格的學習解除了對 MBON-m1 抑制者的抑制——而且明說兩者沒有被區分（該來源頁 3.7 節）。所以它不能被引成「幼蟲也量到 KC→MBON 壓低」。

## 引用時的陷阱

1. **Tomchik 2009 的「增強」不是突觸增強。** KC 軸突裡的鈣變大只是「可能送出較多訊號」的間接指標；洗掉藥物後似乎回落（單一範例）。它與 Hige 2015 的 LTD 方向看似相反，但量的不是同一個東西，不能當成矛盾，也不能當成 Handler 2019 增強的前驅證據。
2. **Hige 2015 的「九成」是電荷總量。** 電流一開始的峰值大致保留，少掉的是之後的持續段。
3. **Hige 2015 只活化可取代嫌惡電擊的 PPL1 型 DAN**，沒看到增強不代表不存在；逆向「無效」與 Handler 2019 逆向「增強」的不同，見 [[syn-contradictions]] 1.1。
4. **Handler 2019 的增強證據較薄**：離體只有 −1.2 s 一點顯著；在體實驗是順向、逆向交替訓練，逆向造成的增強只把前一次順向壓低的反應部分拉回。
5. **改變在突觸前還是突觸後未定**（Hige 2015 自陳）。Cohn 2015 直接量了 KC 突觸前末梢的鈣，看到它隨多巴胺逐格改變，但沒有量**配對後**的末梢鈣，所以仍沒回答配對造成的減弱在哪一側（見 [[c-presynaptic-calcium]]）。Felsenberg 2018 引言把突觸前減弱列為已知，合併引用的文獻包括 Tomchik 2009 與 Hige 2015；本庫對這兩篇的紀錄並不支持這個說法（Tomchik 量到的是 KC 鈣反應**變大**）。
   **2026-11-13 更新：突觸後那一側現在有直接證據，但沒有因此裁決掉突觸前。** [[s-pribbenow-2022-postsynaptic-plasticity]] 在 TTX 下繞過 KC，只刺激 MBON 樹突就誘發出改變，並證明 M4/6 上的 nAChR α5、α2 與 Dlg 是獎賞記憶所必需。三點限制同時成立：幅度只有約 5–6%、方向是增強而非減弱、而且對**嫌惡**記憶找不到突觸後的需求（降低七個 α 次單元中只有 α7 有影響）。作者自己說突觸前機制並未被排除，兩側可能同時改變。另外該篇沒有驗證任何一個 RNAi 的降低效率（該來源頁第五節第 1 條），所以「只有 α5 有效」這種陳述的分量取決於六個陰性結果。
6. **Cohn 2015 的「配對減弱」有兩個條件。** 離體實驗是從已被增強的狀態開始配對；活體實驗量的是配對氣味對未配對氣味的比值，比值下降也可能來自未配對氣味被增強。
7. **「不配對」的時間尺度兩篇對不上。** Cohn 2015 相隔 ＞ 45 s 讓 γ4 突觸變強；Handler 2019 相隔 6 s 幾乎不變。見 [[syn-contradictions]] 1.3，未裁決。
8. **現有規則只處理與 DAN 配對的氣味。** Felsenberg 2017 的 CS− 反應變大發生在沒有與糖配對的氣味上，本頁整理的規則無法直接解釋（[[syn-contradictions]] 3.7）。Ichinose 2015 的模型是 MBON-α1 回頭讓同格的 PAM-α1 更活躍、延長多巴胺釋放（見 [[t-mbon-dan-feedback]]）；這隱含配對後 CS+ 仍能驅動 MBON-α1，與「順向配對讓突觸變弱」有張力（[[syn-contradictions]] 3.6）；Ichinose 2015 本身沒有量突觸變強或變弱。
9. **樹突沒變不等於輸出沒變。** Felsenberg 2018：學習讓 M6 軸突的 CS+ 反應變大，樹突卻看不出差別；作者以鄰格 MVP2 的抑制性輸入作用在 M6 樹突根部附近解釋。只量樹突會漏掉這類網路造成的改變。

10. **Huang 2024 的「DAN 被抑制時突觸變強」與 Hige 2015 在 γ1pedc 的直接量測牴觸。** 模型在 γ1 模組也用這條規則；Hige 2015 讓多巴胺比氣味早約 2.0 s，突觸完全不變。Huang 自己的圖 3f 中，MBON-γ1pedc>α/β 對吸引氣味 CS− 的反應在訓練中途也是**下降**（模型歸因於感覺適應），沒看到變強。⚠️ 矛盾｜未裁決，見 [[syn-contradictions]] 1.9。另外 Huang 量的是 MBON 對氣味的放電，不是 KC→MBON 的突觸電流；※ 推論：放電改變可能混有回饋與鄰格 MBON 的影響（比照陷阱 9）。

11. **兩條本批的「減弱」量的不是同一個東西。** [[s-dylla-2017-trace-conditioning-dan-plasticity]] 量的是 KC 軸突的鈣（整個區室數百顆 KC 的總和，用一般的細胞質 GCaMP3，不是突觸前專用的感測器），[[s-yamada-2023-second-order-conditioning]] 量的是 MBON 的**次閾值去極化平台**（氣味期間 0–20.6 秒的平均），而庫內其他篇多半報峰值或放電數。Yamada 2023 的峰值振幅沒有改變（p＝0.87），所以如果只看峰值，這個減弱根本看不到。

12. **Dylla 2017 的「變小」要和它的基線漂移一起讀。** 該篇圖 2D、4A 的軌跡在刺激後普遍緩慢漂到基線以下，**訓練前後、配對與不配對兩組都有**（該來源頁第五節第 2 條）。而且不配對組的 CS 反應一路往下掉（可能是疲乏、氣味變淡或漂白，作者自承分不出），所以「配對組相對較大／較小」的比較基準本身在移動。

13. **Aso 2019 的「增強」是模型裡的參數，不是量到的突觸。** 該篇的全部證據是行為 PI；「一氧化氮讓突觸變強」與「一氧化氮讓已經變弱的突觸回彈」在行為上一樣，在 KC→MBON 的記錄上才分得開，而該篇沒有做（該來源頁第六節）。引用 w ∝ (1 − D)(1 + N) 時要連這一點一起引。

14. **「推論的減弱」與「量到的減弱」要分開引。** [[s-aso-2014-mbon-valence]] 常被引為突觸變弱的依據，但它沒有量任何 MBON 的生理反應，作者寫的是「最容易解釋」；[[s-aso-2019-nitric-oxide-cotransmitter]] 與 [[s-dylla-2017-trace-conditioning-dan-plasticity]] 同樣沒有量突觸。本頁用法表共 13 列，其中以電生理或「刺激 KC → 量 MBON」的方式量到傳遞改變的是 Hige 2015、Handler 2019、Cohn 2015、Pribbenow 2022（突觸後側）與 Yamada 2023（MBON 次閾值）五列；Felsenberg 2017／2018 與 Huang 2024 量的是 MBON 對**氣味**的反應（可能混有回饋與鄰格 MBON 的影響，見陷阱 9、10）；Tomchik 2009、Dylla 2017 量 KC 自己的鈣；Minnick 2026 是模擬；Aso 2019、Aso 2014b 完全沒有量。

## 相關

- 主題：[[t-dopamine-to-plasticity]]、[[t-timing-rules]]、[[t-memory-updating]]
- 概念：[[c-mb-compartment]]、[[c-camp-signaling]]、[[c-cs-us-timing]]、[[c-presynaptic-calcium]]、[[c-whole-cell-patch-clamp]]
- 實體：[[e-kenyon-cell]]、[[e-mbon]]、[[e-dopaminergic-neuron]]、[[e-gcamp]]、[[e-mbon-gamma4]]、[[e-mbon-gamma1pedc]]、[[e-mbon-gamma2alpha1]]、[[e-mbon-gamma5beta2a]]、[[e-dopamine-receptor]]
- 綜述：[[syn-contradictions]]
- 來源：[[s-hige-2015-heterosynaptic-plasticity]]、[[s-handler-2019-dopamine-receptor-timing]]、[[s-tomchik-2009-camp-dynamics]]、[[s-cohn-2015-coordinated-neuromodulation]]、[[s-felsenberg-2017-re-evaluation]]、[[s-felsenberg-2018-memory-extinction]]、[[s-huang-2024-dopamine-memory-dynamics]]、[[s-minnick-2026-untrained-connectome]]、[[s-pribbenow-2022-postsynaptic-plasticity]]、[[s-dylla-2017-trace-conditioning-dan-plasticity]]、[[s-yamada-2023-second-order-conditioning]]、[[s-aso-2019-nitric-oxide-cotransmitter]]、[[s-aso-2014-mbon-valence]]；另見 [[s-eschbach-2021-learned-innate-valence-integration]]（幼蟲，未列表）
