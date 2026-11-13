---
title: split-GAL4 驅動品系（split-GAL4 driver lines）
created: 2026-10-25
updated: 2026-11-13
tags: [entity, active, mb-learning]
confidence: medium
---

# split-GAL4 驅動品系（split-GAL4 driver lines）

## 是什麼

**驅動品系**是決定「某個外加基因只在哪些神經元表現」的果蠅品系。GAL4 是一種能開啟目標基因的蛋白；在哪些細胞裡製造它，取決於接在前面的調控序列。一般的 GAL4 品系常同時標到很多種細胞。

**split-GAL4** 把 GAL4 拆成兩半：一半負責「抓住 DNA」（DBD），一半負責「啟動表現」（AD），各由一段不同的調控序列控制。只有兩段序列都開啟的細胞，兩半才湊得成完整的 GAL4（Hige 2015 的說明）。這樣能把表現範圍縮到少數幾型、甚至一顆神經元。在本庫，它主要用來只讓特定的 [[e-dopaminergic-neuron]]（DAN）帶上光敏感通道 [[e-cschrimson]]。

另一套互不干擾的系統 LexA 常與它並用：GAL4 標 DAN，LexA 標要記錄的 MBON 或 KC。

## 版本與規模（本庫用到的品系）

| 品系 | 來源 | 兩半各由什麼控制（AD／DBD） | 標記什麼 |
|---|---|---|---|
| **MB320C** | Hige 2015 寫「we created」；Aso 2016 把它的影像指向 Aso et al. 2014a；**[[s-aso-2014-mbon-valence]]（2014-12 刊出，早於 Hige 2015）圖 6K 已用它標 PPL1-γ1pedc** | TH／22B12 | **只標一顆 PPL1-γ1pedc**（[[e-ppl1-gamma1pedc]]） |
| **MB099C** | Hige 2015 新做 | TH／73F07 | ⚠️ 兩篇說法不同：Hige 2015 說**四型 PPL1**（γ2α′1、α′2α2、α′3、α3），Aso 2016 說 PPL1-γ2α′1 ＋ PPL1-α′2α2 **兩型**；兩篇都說它不標 PPL1-γ1pedc。見 [[e-mb099c]]、[[syn-contradictions]] 1.4 |
| MB438B | [[s-aso-2014-mb-architecture]] 表 1 中 PPL1-γ1pedc 的專一品系 | R30E11／R22B12；AD 插在 attP40（基因組上預先設好、供外加基因插入的固定位置） | PPL1-γ1pedc；依 [[s-aso-2014-mbon-valence]] 表 2 **另弱標 PPL1-α2α′2**。Hige 2015 **刻意不用**，理由見下 |
| **MB042B** | Handler 2019 | R58E02／R22E04 | PAM 群（涵蓋哪些區室，論文沒列：？待查）；AD 半與 [[e-r58e02]] 同一段序列 |
| **MB504B** | Handler 2019；Felsenberg 2017、2018 也用 | 52H03／TH | Handler：PPL 群中**支配六個區室**的一部分（沒列哪六個）；Felsenberg 2017 延伸圖 6c：四型 PPL1（γ1pedc、γ2α′1、α′2α2、α3）。兩者如何對應見 [[e-mb504b]] |
| MB630B | Aso 2016 新做 | VT026773／R72B05 | PPL1-α3（一型） |
| MB043C、MB213B、MB315C＋MB109B | Aso 2016 | 未列 | PAM-α1；支配 β1、β2 的 PAM；支配 γ5、β′2a 的 PAM（後兩組各兩型） |
| MB299B；MB310C、MB323B；MB008B | Ichinose 2015（引 Aso et al. 2014a） | 未列 | PAM-α1（[[e-pam-alpha1]]）；MBON-α1；α/β KC |
| MB296B；MB052B；MB077C；MB112C（延伸圖 6i 寫 MB122C）；MB058B；MB308B | Felsenberg 2017 | 未列 | PPL1-γ2α′1（[[e-ppl1-gamma2alpha1]]）；五型 V2 群 MBON；MBON-γ2α′1（[[e-mbon-gamma2alpha1]]）；MVP2（[[e-mbon-gamma1pedc]]）；PPL1-α′2α2；PPL1-α′3（α3 弱） |
| MB011B；MB027B | Pribbenow 2022（引 Aso et al. 2014a） | 該篇未寫：？待查 | M4/6 四型 MBON（γ5β′2a、β′2mp、β2β′2a、β′2mp bilateral）；α′3 的 MBON（該篇以複數稱呼，未寫幾型：？待查） |
| **SS02163**（方法另寫 SS02163f）；**SS02108** | Eschbach 2021（**幼蟲**） | 52H01／40F09；13D05／40F09 | 幼蟲 MBON-m1；幼蟲 CN-33 與 MB2ON-86（每側各兩顆），並微弱標記腹神經索的局部中間神經元。⚠️ 該篇方法與品系表稱這一條為「CN-4」，結果節稱 CN-33（見該來源頁第五節） |
| SS67221、SS45234（SMP108）；SS33917（SMP353／354）；MB043-split-LexA（PAM-α1） | Yamada 2023 新做 | MB043-split-LexA ＝ 58E02-ZpLexADBD（JK22C）／32D11-p65ADZp（JK73A）；其餘未列 | 兩條獨立的 SMP108 品系；SMP353／354；只標 PAM-α1 的 LexA 版本 |
| SS33917、SS33918（行為）；SS67249（電生理） | Aso 2023（與 Shuai et al. 2023 同期發表的新品系集合） | 未列 | 迎風神經元 UpWiN（SS33917／SS33918 各標相似的 8–11 顆；SS67249 只標 1–3 顆） |

### 品系 → 細胞型的對照（Aso 2014a 表 1、Aso 2014b 表 2）

本庫其他來源引用的品系，多半只寫品系名、不寫它標到誰。兩篇 Aso 2014 把對照印了出來，以下只列庫內用得到的部分（括號＝弱、隨機或只在部分報導基因下可見，依 Aso 2014b 表 2 圖說；DAN 那幾列取自 Aso 2014a 表 1）。

| 品系 | 標到的細胞型 | AD／DBD（Aso 2014b 表 2 有列者） |
|---|---|---|
| MB011B | MBON-γ5β′2a、MBON-β′2mp、MBON-β′2mp_bilateral | R14C08／R15B01 |
| MB002B、MB210B | 同上三型的子集（MB002B：(γ5β′2a)、β′2mp；MB210B：γ5β′2a、β′2mp、(β′2mp_bilateral)） | R12C11／R14C08；R15B01／R27G01 |
| MB027B | MBON-α′3m、MBON-α′3ap | R24H08／R53F03 |
| MB052B | MBON-α2sc、(α2p3p)、(α′3m)、α′3ap、α′1（V2 群五型） | R71D08／R11F03 |
| MB077B、MB077C | MBON-γ2α′1 | R25D01／R19F09（兩條同一對增強子，差在 AD 的插入位點） |
| MB082C；MB093C | MBON-α3 ＋ MBON-α′2；MBON-α3、(α′2) | R40B08／R23C06；R73H08／R40B08 |
| MB083C、MB110C | MBON-γ3 與 MBON-γ3β′1（兩型同時，無法分開） | R52G04／R94B10；R20A02／R94B10 |
| MB085C、MB112C、MB262B | MBON-γ1pedc>α/β | R52H01／R52B07；R93D10／R13F04；R52B07／R52H01 |
| MB298B | MBON-γ4>γ1γ2 | R53C03／R24E12 |
| MB310C | MBON-α1 | R52G04／R17C11 |
| MB434B；MB433B | MBON-γ4>γ1γ2 ＋ MBON-β1>α；(γ4>γ1γ2) ＋ β1>α | R30E08／R53C10；R30E08／R11C07 |
| MB438B | PPL1-γ1pedc，**另弱標 PPL1-α2α′2** | R30E11／R22B12 |
| MB296B、MB439B；MB058B；MB304B；MB065B、MB060B | PPL1-γ2α′1；PPL1-α′2α2；PPL1-α′3；PPL1-α3（**但 Aso 2014a 圖 11F 說 MB060B 在四型 PPL1 表現**） | Aso 2014a 表 1 未列 |
| MB043B；MB312B；MB315C、MB335C；MB109B | PAM-α1；PAM-γ4<γ1γ2 與 PAM-γ4（兩型同時）；PAM-γ5；PAM-β′2a | Aso 2014a 表 1 未列 |

AD／DBD 欄取自兩篇原文的方法與基因型清單（Hige 2015 方法；Handler 2019 STAR Methods 基因型表；Aso 2014b 表 2）。TH 指合成多巴胺的酵素酪胺酸羥化酶的調控序列；22B12、73F07、R58E02、R22E04、52H03 等是調控序列片段的編號（基因型寫成「片段名-AD」「片段名-DBD」）。表中的「一顆」照 Hige 原文 a single neuron；左右腦是否各一顆，原文沒說：？待查。

**常與它並列、但不是 split-GAL4 的品系**：TH-GAL4（[[e-th-gal4]]；Hige 用作正對照，即已知應該有效、用來確認方法可行的組；Handler 與 DDC-Gal4 一起用來在 DAN 表現 VMAT-pHluorin；Felsenberg 2017 用來阻斷 PPL1）；R58E02-GAL4／-LexA（[[e-r58e02]]；標記範圍各篇寫法不同：Handler 2019 基因型表標「γ4–5 DANs」，Cohn 2015 說「包含」支配 γ4、γ5 的一部分 DAN，Felsenberg 2017 延伸圖 6a、6o 說兩個版本都標 13 型 PAM，見 [[syn-contradictions]] 1.5）；73F07-LexA（Handler，γ2 DAN）；VT045661-LexA（Aso 2016，PPL1-γ1pedc）；VT1211-GAL4／-LexA（Felsenberg 2018，M4β′ 與 M6）；Tomchik 2009 的 238Y、c739（[[e-c739-gal4]]）、c305a、1471、c316、GH146 都是一般 GAL4。

## 庫內誰用了它

| 來源 | 用了哪些 | 用來做什麼 |
|---|---|---|
| [[s-tomchik-2009-camp-dynamics]] | **未使用**（只用一般 GAL4，且沒有操弄 DAN） | — |
| [[s-hige-2015-heterosynaptic-plasticity]] | MB320C、MB099C | MB320C 只活化 γ1pedc 的 DAN，誘發該區 MBON 的突觸變弱；MB099C 活化鄰區 DAN，檢查多巴胺會不會越界，並用來活化 α2 區 |
| [[s-handler-2019-dopamine-receptor-timing]] | MB042B、MB504B | 行為實驗中以光活化 PAM 或 PPL；閉迴路用 MB042B 驅動 ChrimsonR |
| [[s-aso-2016-dan-cell-type-rules]] | MB320C、MB099C、MB630B、MB043C、MB213B、MB315C＋MB109B | 每組品系驅動 CsChrimson，比較各型 DAN 寫入與更新記憶的規則；三組一次活化兩型，因為只活化一型時記憶太弱 |
| [[s-ichinose-2015-reward-recurrent-circuit]] | MB299B、MB310C、MB323B、MB008B | 以 shibire^ts 阻斷（[[e-shibire-ts]]）、RNAi 或 dTrpA1 活化 PAM-α1、MBON-α1、α/β KC |
| [[s-felsenberg-2017-re-evaluation]] | MB504B、MB296B、MB052B、MB077C、MB112C、MB058B、MB308B 等 | 在記憶再活化期間阻斷特定 DAN 或 MBON |
| [[s-felsenberg-2018-memory-extinction]] | MB504B、MB112C | 阻斷 PPL1 群（消退照常）；MVP2 的成像與解剖 |
| [[s-cohn-2015-coordinated-neuromodulation]] | **主文未具名**（稱 sparse driver lines；γ2 DAN、各 γ MBON 的品系名 ？待查） | 讓單一型 MBON 表現 P2X2 或 GCaMP6s |
| [[s-aso-2014-mb-architecture]] | **本庫所有蕈狀體 split-GAL4 品系的製作來源**：掃約 7,000 個 GAL4 品系 → 做出約 400 個半套品系 → 篩 2,500 種以上的組合 → 400 個以上強表現的組合 → 選定 92 個 | 為蕈狀體的每一型細胞做出專一品系，供後續功能實驗使用；92 個品系的基因型與標到的細胞型列在補充檔 1（本庫未取得），共軛焦影像在 janelia.org/split-gal4 |
| [[s-aso-2014-mbon-valence]] | 31 條 MBON 品系（表 2；25 條用於光遺傳篩檢、23 條用於 shibire 初篩）＋ MB438B（PPL1-γ1pedc） | 逐型光遺傳活化、阻斷與睡眠篩檢；以插在同一基因組位置的報導基因估各型的表現量；方法定「兩條品系都看到才指派功能」 |
| [[s-aso-2019-nitric-oxide-cotransmitter]] | MB320C、VT045661-LexA、R52H03∩TH、R58E02∩DDC、MB247-switch、Gr66a-GAL4，以及用於細胞分選的多條 DAN 品系 | 一品系一型地比較價性有沒有反轉；以細胞核標記的報導基因分選細胞做 RNA 定序；MB247-switch 做成蟲期限定的 KC 敲低 |
| [[s-pribbenow-2022-postsynaptic-plasticity]] | MB011B、MB027B、MB112C、MB461B、MB369B | 在指定的 MBON（M4/6、α′3）或稀疏 KC 表現 RNAi、GCaMP6f 或 Shi。**作者註明基因型太複雜時改用 VT1211-GAL4 取代 MB011B**，所以同一結論的不同實驗取用 M4/6 的工具不一定相同 |
| [[s-eschbach-2021-learned-innate-valence-integration]] | **幼蟲**：15 個 MBON 品系（涵蓋 24 型中的 18 型）；功能實驗用 SS02163（MBON-m1）與 SS02108（CN-33） | 逐型光活化判定正價值或負價值；鈣成像與 Kir2.1 阻斷 |
| [[s-yamada-2023-second-order-conditioning]] | 既有：MB043C、MB109B、MB315C、MB213B、MB312C、MB032B、MB196B、SS01308、MB319C、empty-split；新做：SS67221、SS45234（SMP108）、SS33917（SMP353／354）、MB043-split-LexA（PAM-α1） | 活化或阻斷各格 PAM 做二階制約；以兩條獨立的 SMP108 品系做阻斷，是該篇解剖專一性的主要防線（兩條的完整表現範圍在未取得的補充圖 8-1：？待查） |
| [[s-aso-2023-upwind-neurons]] | 約 63 條新品系做活化篩選；UpWiN 用 SS33917、SS33918（行為）與 SS67249（電生理）；DAN 用 MB043C、MB213B、MB312C、MB109B＋MB315C；MBON 用 MB310C、MB082C、MB077B、MB083C | 光遺傳篩選迎風表型；圖 7C 的 shibire 實驗以三組對照與實驗組並比，依該篇基因型清單，對照之一只帶半套品系（VT007746-p65ADZp）加效應基因 |
| [[s-huang-2024-dopamine-memory-dynamics]] | MB504B、MB502B、MB065B、MB304B、MB085C、MB093C、MB080C、MB077B、MB542B（皆來自 Janelia，與 w1118 回交五代） | 在五型 PPL1 與六型 MBON 表現電壓指示劑 pAce；MB085C 驅動 TnT 或 CsChrimson 阻斷或活化 MBON-γ1pedc>α/β；MB093C 驅動 TnT 阻斷 MBON-α3；MB065B 驅動 jGCaMP7b 做 PPL1-α3 的鈣成像對照 |

## 已知的問題（解讀實驗的陷阱）

- **「一個品系」不等於「一型細胞」。** MB099C 同時活化多型 PPL1（幾型，兩篇說法不同，見上表）；Aso 2016 有三組品系各活化兩型；TH-GAL4 標多數 PPL1、少數 PAM 以及蕈狀體以外的許多 DAN。讀到「活化 MB099C」時，要記得是不止一型一起放電。
- **品系不同會混進比較。** Hige 2015 比較 γ1（MB320C，一顆 DAN）與 α2（MB099C，依 Hige 為四型 DAN、依 Aso 2016 為兩型）的誘發門檻（要多少次「氣味＋光」配對才會讓突觸變弱；見 [[e-mushroom-body]]），兩個品系的通道表現量與每次放出的多巴胺量可能不同。行為上，MB099C 代替電擊的效果也遠低於 MB320C（補充圖 S1F：？待查）。Aso 2016 只為 MB320C 與 MB099C 引了放電資料（引 Hige 2015），其餘四組沒有放電或多巴胺釋放的校準，「學得慢」「記得久」的差異可能部分來自活化強度。
- **涵蓋範圍沒有列出。** Handler 2019 的 MB504B（六個區室）與 MB042B 都沒列出支配哪些區室（MB504B 的型別見 Felsenberg 2017 延伸圖 6c，對應方式是 ※ 推論，見 [[e-mb504b]]），而全篇的分子與突觸實驗只在 γ4 做。行為結果可能混有 γ4 以外區室的貢獻，作者也承認行為由多區室合成。
- **品系與細胞型的對照表沒印出來。** Huang 2024 列了九個 split-GAL4 品系，但哪個品系量哪一型，寫在延伸表 1，而 PDF 只有表題、沒有內容（？待查）。除了圖說直接寫出基因型的幾組（MB504B、MB085C、MB093C、MB065B），其餘品系對應哪一型不能自行配對。
- **品系名末尾的字母是 AD 的插入位點，不是版本序號。** 依 [[s-aso-2014-mb-architecture]] 補充檔 1 圖說與 [[s-aso-2014-mbon-valence]] 表 2 圖說：所有 ZpGAL4DBD 都插在 attP2，品系名末尾 A ＝ su(Hw)attP8、B ＝ attP40、C ＝ VK00027。**所以 MB043B 與 MB043C、MB062B 與 MB062C、MB077B 與 MB077C 是同一對增強子的不同版本，不能互相代用**（Aso 2014a 表 1 的 PAM-α1 寫 MB043B，而 [[s-aso-2016-dan-cell-type-rules]] 用的是 MB043C）。表現量與插入位點有關，所以兩個版本的效果強弱未必相同。
- **「表 1 列出某品系」不等於「該品系只標這一型」。** Aso 2014a 圖 11F 明說 MB060B 在四型 PPL1 表現，而表 1 把它列在 PPL1-α3 那一列。反方向的完整對照（品系 → 它標到的全部細胞型）在補充檔 1，本庫未取得：？待查。Aso 2014b 表 2 是庫內目前唯一印出來的反方向對照，但只涵蓋 MBON 的 31 條。
- **表現樣式會隨報導基因與插入位點改變。** Aso 2014a 方法明說：92 個品系在 attP18 與 VK00005 兩個位點各測一次，樣式一致但強度差很多，而且 VK00005 的兩種報導基因偶爾會顯出 attP18 看不到的脫靶細胞。Aso 2014b 也說明，所以它刻意讓指示用的報導基因與效應基因插在同一位置。比較不同論文用「同一個品系」的結果時，表現量未必可比。
- **同一篇裡也會換品系。** Aso 2019 的圖 6 在不同格用不同的 γ1pedc 驅動品系（B、C 與 TH 突變組用 VT045661-LexA，D 用 MB320C），E 格的野生型與 NOS-RNAi 用哪個則沒有寫（？待查）。跨格比較 PI 時要先確認品系。Pribbenow 2022 在基因型太複雜時以 VT1211-GAL4 取代 MB011B，同屬此類。
- **插入位點會互相干擾。** Hige 2015 不用 MB438B，因為它的 AD 插在 attP40，與該篇標 MBON 的 LexA 品系同一位點，可能發生 transvection（同源染色體上相同位點的調控元件互相影響），讓 GAL4 與 LexA 在同一批細胞表現；後果是光敏感通道也出現在被記錄的 MBON 上（引 Mellert & Truman 2012）。
- **同一段調控序列可出現在不同品系。** 73F07 是 Hige 的 MB099C 的 DBD，也是 Handler 標 γ2 DAN 的 LexA；25D01 在 Hige 標 MBON-γ2α′1、在 Handler 標「γ2 MBON」。※ 推論：兩篇可能標到相同或重疊的細胞，但 split-GAL4、GAL4 與 LexA 版本的表現範圍不一定相同，兩篇沒有比對：？待查（另見 [[e-mbon]]）。

## 相關

- 工具：[[e-cschrimson]]、[[e-gcamp]]、[[e-shibire-ts]]、[[e-p2x2]]
- 細胞：[[e-dopaminergic-neuron]]、[[e-mbon]]、[[e-kenyon-cell]]、[[e-ppl1-gamma1pedc]]、[[e-ppl1-gamma2alpha1]]、[[e-pam-alpha1]]
- 品系：[[e-mb099c]]、[[e-mb504b]]、[[e-r58e02]]、[[e-th-gal4]]、[[e-c739-gal4]]、[[e-238y-gal4]]
- 概念：[[c-us-substitution]]、[[c-mb-compartment]]
- 綜述：[[syn-contradictions]]
- 來源：[[s-hige-2015-heterosynaptic-plasticity]]、[[s-handler-2019-dopamine-receptor-timing]]、[[s-tomchik-2009-camp-dynamics]]、[[s-aso-2016-dan-cell-type-rules]]、[[s-ichinose-2015-reward-recurrent-circuit]]、[[s-felsenberg-2017-re-evaluation]]、[[s-felsenberg-2018-memory-extinction]]、[[s-cohn-2015-coordinated-neuromodulation]]、[[s-huang-2024-dopamine-memory-dynamics]]、[[s-aso-2014-mb-architecture]]、[[s-aso-2014-mbon-valence]]、[[s-aso-2019-nitric-oxide-cotransmitter]]、[[s-pribbenow-2022-postsynaptic-plasticity]]、[[s-eschbach-2021-learned-innate-valence-integration]]、[[s-yamada-2023-second-order-conditioning]]、[[s-aso-2023-upwind-neurons]]
