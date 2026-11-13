---
title: 前饋抑制（feedforward inhibition）與 MBON 之間的抑制
created: 2026-11-13
updated: 2026-11-13
tags: [concept, active, mb-memory-dynamics]
confidence: low
---

# 前饋抑制（feedforward inhibition）與 MBON 之間的抑制

**同一個上游同時興奮目標神經元與一顆抑制性神經元，後者再壓住目標。** 在本庫，這個詞幾乎都用在蕈狀體輸出神經元（MBON）身上：學習讓一顆抑制性 MBON 對受訓氣味變安靜，它的下游就被「解除抑制」（disinhibition），反應相對變大。下游可以是另一顆 MBON、一顆多巴胺神經元，或蕈狀體外的中間神經元；各篇用法不同，見陷阱 1。

**本頁用語**（每頁可單獨查閱，故重複列出）：

- **KC、MBON、DAN**：Kenyon 細胞（在蕈狀體裡代表氣味）、蕈狀體輸出神經元（推動靠近或走開）、多巴胺神經元（送獎懲訊號）。學習改變的是 KC→MBON 突觸，見 [[c-kc-mbon-plasticity]]。
- **區室**：蕈狀體的葉沿長度分成一格一格，每格一型 DAN、一型 MBON，見 [[c-mb-compartment]]。細胞以區室命名，例如 MBON-γ1pedc>α/β（樹突在 γ1pedc、軸突伸到 α/β 葉）。
- **MVP2**：MBON-γ1pedc>α/β 的舊名，放 GABA，活化時推動靠近。**M4β′、M6**：放麩胺酸、推動走開的 MBON（M6＝MBON-γ5β′2a）。
- **GABA、麩胺酸、乙醯膽鹼**：三種傳遞物質。GABA 在果蠅腦中是抑制性；麩胺酸在本庫各篇被假設為抑制性（作用在氯離子通道），多半沒有直接量過；乙醯膽鹼是興奮性。
- **解除抑制**：抑制者變安靜，被抑制者因此反應變大。
- **CS+**：訓練時配了獎懲的氣味。

## 怎麼判定

要說一條連線是「前饋抑制」，需要三件事，本庫各篇做到的程度不同：(1) 解剖上有接點（光學重疊或電顯突觸）；(2) 正負號是抑制（傳遞物質推定、受體操作或電生理）；(3) 抑制者與目標收同一上游（多為 KC）。

## 庫內的用法

| 來源 | 路徑 | 怎麼用／得到什麼 |
|---|---|---|
| [[s-aso-2014-mb-architecture]] | MBON→MBON（葉內） | 三型 MBON 的軸突送回葉內別格：γ4>γ1γ2（麩胺酸）、β1>α（麩胺酸）、γ1pedc>α/β（GABA）。12 型屬單層讀出，α1–α3 的讀出是四層「前饋網路」。**只有影像重疊，傳遞物質是免疫染色推定，沒有功能實驗** |
| [[s-aso-2014-mbon-valence]] | MBON→MBON（模型） | 圖 14 假設麩胺酸 MBON 抑制 GABA 與乙醯膽鹼 MBON、GABA MBON 抑制麩胺酸 MBON；嫌惡學習讓 γ1pedc 的 GABA MBON 對 CS+ 變弱 → 麩胺酸 MBON 被放開 → 果蠅走開。**全部是假設，沒有 MBON 生理記錄** |
| [[s-felsenberg-2018-memory-extinction]] | MBON→MBON（經典前饋抑制） | KC 同時興奮 MVP2 與 M4β′／M6，MVP2 再抑制後兩者。電顯數到 MVP2→M4β′ 47 個突觸、→M6 17（右）／16（左）個；M6 的接點集中在樹突根部，作者推論可「分流」整棵樹突。用來解釋：學習效果只在 M6 的軸突看得到、樹突看不到；消退後兩筆記憶在 M6 相抵。抑制的正負號引 Perisse 2016，不是本篇量的 |
| [[s-aso-2016-dan-cell-type-rules]] | MBON→MBON | 用 γ1pedc（GABA）到 α 葉的前饋連線解釋兩份記憶「非線性整合」：若相加應約 −0.14，實測 −0.38。本篇沒有檢驗這條連線 |
| [[s-pribbenow-2022-postsynaptic-plasticity]] | MBON→MBON | 離體腦加 TTX 排除了 MVP2 的去抑制；作者把它列為離體（增強）與活體（減弱）方向相反的可能原因之一 |
| [[s-eschbach-2021-learned-innate-valence-integration]] | MBON→MBON（幼蟲，作者稱「側向抑制」） | 依 Eichler 2017 的連結體，數到 6 處負價值 MBON 抑制正價值 MBON、3 處反方向；推測學習時放大兩側差距。只存在於部分 MBON 之間，作者因此轉往下一層找整合點 |
| [[s-huang-2024-dopamine-memory-dynamics]] | MBON→DAN（作者稱「回饋」） | hemibrain 上 MBON-γ1pedc>α/β 接到 PPL1-α3。阻斷它（TnT），PPL1-α3 對 CS+ 不再「由降轉升」；訓練時持續活化它（2 × 2 設計，每組 12 隻），5 分鐘記憶正常、3 小時記憶消失；在 PPL1-α3 降低 GABA 或麩胺酸受體，雙向編碼被破壞 |
| [[s-aso-2023-upwind-neurons]] | MBON→蕈狀體外中間神經元 | 電生理直接看到 MBON-α1 抑制迎風神經元（17 顆中 4 顆）、MBON-α3 興奮它（11 顆中 3 顆）；同時活化時興奮被抵掉（約 0.43 → 0.04，※ 從圖判讀，無統計檢定）。獎賞訓練後迎風神經元對 CS+ 由約 0.6 升到約 3.7 mV，作者以 MBON-α1 的去抑制解釋，但同一實驗沒有量 MBON-α1 |
| [[s-yamada-2023-second-order-conditioning]] | MBON→兩層中間神經元→別格 DAN | 作者稱為「前饋迴路」：MBON-α1 → SMP353/354 → SMP108 → 多型獎賞 DAN。學習讓 MBON-α1 對 S1 變小、下游被解除抑制，才能教出二階記憶（見 [[c-second-order-conditioning]]）。**這一步作者寫成條件句（if glutamate is inhibitory），沒有量正負號** |

## 引用時的陷阱

1. **「前饋」在本庫至少有四種意思，同一顆神經元會被叫成相反的名字。** (a) Felsenberg 2018：經典的前饋抑制（KC 同時驅動 MVP2 與 M6）。(b) Aso 2014a／2014b：MBON 軸突伸到別格、不回自己樹突的「前饋網路」，其中兩型是麩胺酸、不一定是抑制。(c) Yamada 2023：老師區室到學生區室的「前饋迴路」，中間兩層是乙醯膽鹼（興奮性），抑制只在第一步。(d) Huang 2024 的圖 1 把 KC→MBON 叫前饋、MBON→DAN 叫回饋，所以**同一顆 MBON-γ1pedc>α/β，在 Felsenberg 2018 與 Aso 2014a 是前饋，在 Huang 2024 是回饋**（它的軸突同時伸到別格 MBON 與別格 DAN）。引用時要寫明下游是誰。
2. **正負號多半是推定。** 直接量到抑制的只有 Aso 2023 的電生理（MBON-α1→迎風神經元）與 Huang 2024 的受體操作；Felsenberg 2018 引用他篇，Aso 2014a 用免疫染色推定傳遞物質。「麩胺酸＝抑制」在 Yamada 2023 是條件句；[[s-ichinose-2015-reward-recurrent-circuit]] 則設想 MBON-α1 的麩胺酸回頭**興奮** PAM-α1。兩者下游不同，Yamada 2023 來源頁不列為跨篇矛盾。
3. **鈣成像常看不到抑制。** Aso 2023 的電生理看得到 MBON-α1 的抑制，離體鈣成像單獨活化 MBON-α1 卻看不到下降；Huang 2024 也指出鈣成像抓不到放電減少。「鈣訊號沒降」不等於「沒被抑制」。
4. **解除抑制與突觸增強在讀數上分不開。** 下游反應變大，可以是抑制者變安靜，也可以是下游自己的突觸變強。Aso 2023 承認 β1 區室的可塑性也可能有貢獻；Felsenberg 2018 的「分流」是由接點位置推論，沒有電生理驗證。
5. **APL 不屬於本頁。** APL 是對 KC 的抑制性**回饋**（[[e-apl-neuron]]），本庫來源沒有把它當成 KC→MBON 的前饋抑制使用；Minnick 2026 的連結體模型還把它判成興奮性（見 [[c-sparse-coding]] 陷阱 3）。

## 相關

- 主題：[[t-mbon-dan-feedback]]、[[t-memory-updating]]、[[t-mbon-to-action]]、[[t-innate-learned-integration]]
- 概念：[[c-valence-coding]]、[[c-kc-mbon-plasticity]]、[[c-memory-extinction]]、[[c-second-order-conditioning]]
- 實體：[[e-mbon]]、[[e-mbon-gamma1pedc]]、[[e-mbon-gamma5beta2a]]、[[e-mbon-alpha1]]、[[e-mbon-alpha3]]、[[e-hemibrain]]、[[e-catmaid]]
- 待開頁面：`e-mbon-beta2mp`（M4β′）、`e-smp108`、`c-convergence-neuron`
