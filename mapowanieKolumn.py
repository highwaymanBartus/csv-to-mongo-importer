from datetime import datetime

COLUMN_MAP = {
    "id": {
        "meta": {
            "value": "Kod badanego 1"
        }
    },

    "dane": {
        "raw":{
            "Sygnatura czasowa": "Sygnatura czasowa",
            "Kod badanego 2": "Kod badanego 2",
            "Płeć": "Podaj swoją płeć",
            "Data urodzenia": "Podaj swoją datę urodzenia",
            "Status HL": "Status HL",
            "Status ET": "Status ET",
            "Status testów poznawczych": "Status testów poznawczych",
            "Status biometrii": "Status biometrii",
            "Miejsce badania": "Miejsce badania"
        },
        "summary":{
            "Wiek": "Wiek",
            "Dni badanego": "Wiek w dniu badania (dni)",
            "Minuty trwania lekcji": "Czas trwania samej lekcji (minuty)"
        }
    },

    "zmęczenie":{
        "raw":{
            "NASA TLX MentalDemand": "NASA TLX MentalDemand",
            "NASA TLX PhysicalDemand": "NASA TLX PhysicalDemand",
            "NASA TLX TemporalDemand": "NASA TLX TemporalDemand",
            "NASA TLX Performance": "NASA TLX Performance",
            "NASA TLX Effort": "NASA TLX Effort",
            "NASA TLX Frustration": "NASA TLX Frustration",
            "NASA TLX CalculatedTiredness": "NASA TLX CalculatedTiredness"
        },
        "summary":{
            "Różnica sakkad": "diff_liczba_saccades",
            "Różnica trwania fiksacji": "diff_fixation", 
            "Różnica długości sakkady": "diff_dl_saccades",
            "Różnica testów PVT": "diff_pvt",
            "Różnica testów 2-back": "diff_2back",
            "Różnica błędów 2-back": "diff_wtedykiedyniepowinni (blednie_bodziec_jako_cel)",
            "Różnica braku reakcji 2-back": "diff_brak_reakcji_a_powinni",
            "Fatigue_ICA": "Fatigue_ICA",
            "Q1+Q2/Q3+Q4_diff": "Q1+Q2/Q3+Q4_diff",
            "Q1/Q4_diff": "Q1/Q4_diff"
        }
    },

    "pvt": {
        "raw":{
            "PVT kod badanego": "PVT kod badanego"
        },
        "summary":{
            "Średnie PVT przed": "PVT 1 (ms)",
            "SD PVT przed": "PVT 1 SD (ms)",
            "Średnie PVT po": "PVT 2 (ms)",
            "SD PVT po": "PVT 2 SD (ms)",
            "Odfiltrowane >700ms": "odfiltrowane (> 700 ms)"
        }
    },

    "tlx": {
        "raw":{
            "NASA TLX kod badanego": "NASA TLX kod badanego",
            "NASA TLX MentalDemand": "NASA TLX MentalDemand",
            "NASA TLX PhysicalDemand": "NASA TLX PhysicalDemand",
            "NASA TLX TemporalDemand": "NASA TLX TemporalDemand",
            "NASA TLX Performance": "NASA TLX Performance",
            "NASA TLX Effort": "NASA TLX Effort",
            "NASA TLX Frustration": "NASA TLX Frustration",
            "NASA TLX CalculatedTiredness": "NASA TLX CalculatedTiredness"
        }
    },

    "2-back":{
        "raw":{
            "2-back kod badanego": "2-back kod badanego",
            "2-back1 Liczba rekordów": "2-back 1 LiczbaRekordów",
            "2-back1 Liczba sytuacji": "2-back 1 LiczbaSytuacji",
            "2-back1 Liczba poprawnych kliknięć": "2-back 1 LiczbaPoprawnychKliknięć",
            "2-back1 Liczba niepoprawnych kliknięć": "2-back 1 LiczbaNiepoprawnychKliknięć",
            "2-back1 Liczba niepoprawnych braków kliknięć": "2-back 1 LiczbaNiepoprawnychBrakówKliknięć",
            "2-back1 Liczba poprawnych braków kliknięć": "2-back 1 LiczbaPoprawnychBrakówKliknięć",
            "2-back2 Liczba rekordów": "2-back 2 LiczbaRekordów",
            "2-back2 Liczba sytuacji": "2-back 2 LiczbaSytuacji",
            "2-back2 Liczba poprawnych kliknięć": "2-back 2 LiczbaPoprawnychKliknięć",
            "2-back2 Liczba niepoprawnych kliknięć": "2-back 2 LiczbaNiepoprawnychKliknięć",
            "2-back2 Liczba niepoprawnych braków kliknięć": "2-back 2 LiczbaNiepoprawnychBrakówKliknięć",
            "2-back2 Liczba poprawnych braków kliknięć": "2-back 2 LiczbaPoprawnychBrakówKliknięć"
        },
        "summary":{
            "2-back1 Procent poprawnych kliknięć": "2-back 1 ProcentPoprawnychKliknięć",
            "2-back1 Średnia czasów reakcji poprawnych kliknięć": "2-back 1 ŚredniaCzasówReakcjiDlaPoprawnychKliknięć",
            "2-back1 Średnia czasów reakcji niepoprawnych kliknięć": "2-back 1 ŚredniaCzasówReakcjiDlaNiepoprawnychKliknięć",
            "2-back2 Procent poprawnych kliknięć": "2-back 2 ProcentPoprawnychKliknięć",
            "2-back2 Średnia czasów reakcji poprawnych kliknięć": "2-back 2 ŚredniaCzasówReakcjiDlaPoprawnychKliknięć",
            "2-back2 Średnia czasów reakcji niepoprawnych kliknięć": "2-back 2 ŚredniaCzasówReakcjiDlaNiepoprawnychKliknięć"
        }
    },

    "doświadczenie":{
        "raw":{
            "Nauka zdalna": "Czy masz doświadczenie nauki zdalnej?",
            "Nauka zdalna stres": "Jeśli tak, w jakim stopniu nauka w tej formie była dla Ciebie stresująca? (Skala 1-5)",
            "Doświadczenie VR": "Doświadczenie VR",
            "Doświadczenie AR": "Doświadczenie AR",
            "Przedział godzinowy": "Liczba godzin (przedział)"
        }
    },

    "eas-d ws":{
        "summary":{
            "EAS-D WS Niezadowolenie": "Niezadowolenie EAS-D WS",
            "EAS-D WS Strach": "Strach EAS-D WS",
            "EAS-D WS Złość": "Złość EAS-D WS",
            "EAS-D WS Aktywność": "Aktywność EAS-D WS",
            "EAS-D WS Towarzyskość": "Towarzyskość EAS-D WS"
        }
    },

    "stai x1":{
        "summary":{
            "STAI X1 Lęk jako cecha1": "STAI X1 Lęk jako cecha",
            "STAI X1 Lęk jako cecha2": "STAI X1 Lęk jako cecha (2)"
        }
    },

    "quiz":{
        "raw":{
            "Quiz 1": "Quiz 1",
            "Quiz 2": "Quiz 2",
            "Quiz 3": "Quiz 3",
            "Quiz 4": "Quiz 4",
            "Quiz 5": "Quiz 5"
        },
        "summary":{
            "Quiz wynik": "Quiz"
        }
    },

    "tam":{
        "summary":{
            "TAM IS": "TAM IS (ZŁE! - chyba mierzone przed badaniem)",
            "TAM IS%": "TAM IS % (ZŁE!)",
            "TAM PU": "TAM PU",
            "TAM PU%": "TAM PU %",
            "TAM PEU": "TAM PEU",
            "TAM PEU%": "TAM PEU %",
            "TAM PE": "TAM PE",
            "TAM PE%": "TAM PE %",
            "TAM ATU": "TAM ATU",
            "TAM ATU%": "TAM ATU %",
            "TAM ITU": "TAM ITU",
            "TAM ITU%": "TAM ITU %"
        }
    },

    "ueq":{
        "summary":{
            "UEQ Atrakcyjność": "UEQ Atrakcyjność",
            "UEQ Przejrzystość": "UEQ Przejrzystość",
            "UEQ Efektywność": "UEQ Efektywność",
            "UEQ Zależność": "UEQ Zależność",
            "UEQ Poziom stymulacji": "UEQ Poziom stymulacji",
            "UEQ Oryginalność": "UEQ Oryginalność"
        }
    },

    "et": {
        "raw": {
            "ET kod Badanego": "ET kod Badanego",
            "AvatarChatGPTMrtkCanvas Total Time": "AvatarChatGPTMrtkCanvas Total Time",
            "AvatarChatGPTMrtkCanvas Average Gaze Time": "AvatarChatGPTMrtkCanvas Average Gaze Time",
            "BottomMoveHandle Total Time": "BottomMoveHandle Total Time",
            "BottomMoveHandle Average Gaze Time": "BottomMoveHandle Average Gaze Time",
            "CanvasButtonToggleSwitch Variant Total Time": "CanvasButtonToggleSwitch Variant Total Time",
            "CanvasButtonToggleSwitch Variant Average Gaze Time": "CanvasButtonToggleSwitch Variant Average Gaze Time",
            "CanvasButtonToggleSwitch Variant (1) Total Time": "CanvasButtonToggleSwitch Variant (1) Total Time",
            "CanvasButtonToggleSwitch Variant (1) Average Gaze Time": "CanvasButtonToggleSwitch Variant (1) Average Gaze Time",
            "CanvasButtonToggleSwitch Variant (2) Total Time": "CanvasButtonToggleSwitch Variant (2) Total Time",
            "CanvasButtonToggleSwitch Variant (2) Average Gaze Time": "CanvasButtonToggleSwitch Variant (2) Average Gaze Time",
            "CanvasButtonToggleSwitch Variant (3) Total Time": "CanvasButtonToggleSwitch Variant (3) Total Time",
            "CanvasButtonToggleSwitch Variant (3) Average Gaze Time": "CanvasButtonToggleSwitch Variant (3) Average Gaze Time",
            "EraserBigBoxToggle Total Time": "EraserBigBoxToggle Total Time",
            "EraserBigBoxToggle Average Gaze Time": "EraserBigBoxToggle Average Gaze Time",
            "FemaleAvatar_Animation_FakeLipSync Total Time": "FemaleAvatar_Animation_FakeLipSync Total Time",
            "FemaleAvatar_Animation_FakeLipSync Average Gaze Time": "FemaleAvatar_Animation_FakeLipSync Average Gaze Time",
            "Handle Total Time": "Handle Total Time",
            "Handle Average Gaze Time": "Handle Average Gaze Time",
            "MrtkButton Total Time": "MrtkButton Total Time",
            "MrtkButton Average Gaze Time": "MrtkButton Average Gaze Time",
            "NextButton Total Time": "NextButton Total Time",
            "NextButton Average Gaze Time": "NextButton Average Gaze Time",
            "PenBoxToggle Total Time": "PenBoxToggle Total Time",
            "PenBoxToggle Average Gaze Time": "PenBoxToggle Average Gaze Time",
            "Pendulum Total Time": "Pendulum Total Time",
            "Pendulum Average Gaze Time": "Pendulum Average Gaze Time",
            "PendulumPropertiesCanvas Total Time": "PendulumPropertiesCanvas Total Time",
            "PendulumPropertiesCanvas Average Gaze Time": "PendulumPropertiesCanvas Average Gaze Time",
            "PressableButton_32x32mm_IconAndText Total Time": "PressableButton_32x32mm_IconAndText Total Time",
            "PressableButton_32x32mm_IconAndText Average Gaze Time": "PressableButton_32x32mm_IconAndText Average Gaze Time",
            "PrevButton Total Time": "PrevButton Total Time",
            "PrevButton Average Gaze Time": "PrevButton Average Gaze Time",
            "RedoButton Total Time": "RedoButton Total Time",
            "RedoButton Average Gaze Time": "RedoButton Average Gaze Time",
            "RotateHandle (2) Total Time": "RotateHandle (2) Total Time",
            "RotateHandle (2) Average Gaze Time": "RotateHandle (2) Average Gaze Time",
            "RotateHandle (3) Total Time": "RotateHandle (3) Total Time",
            "RotateHandle (3) Average Gaze Time": "RotateHandle (3) Average Gaze Time",
            "ScaleHandle Total Time": "ScaleHandle Total Time",
            "ScaleHandle Average Gaze Time": "ScaleHandle Average Gaze Time",
            "SliderTrack Total Time": "SliderTrack Total Time",
            "SliderTrack Average Gaze Time": "SliderTrack Average Gaze Time",
            "TopMoveHandle Total Time": "TopMoveHandle Total Time",
            "TopMoveHandle Average Gaze Time": "TopMoveHandle Average Gaze Time",
            "Tray Total Time": "Tray Total Time",
            "Tray Average Gaze Time": "Tray Average Gaze Time",
            "UndoButton Total Time": "UndoButton Total Time",
            "UndoButton Average Gaze Time": "UndoButton Average Gaze Time",
            "WhiteboardCollider Total Time": "WhiteboardCollider Total Time",
            "WhiteboardCollider Average Gaze Time": "WhiteboardCollider Average Gaze Time"
        }
    },

    "_external": {
        "raw": {
            "KES": "KES",
            "czy były szczególne sytuacje": "czy były szczególne sytuacje",
            "STRESS_INDEX_S1": "STRESS_INDEX_S1",
            "STRESS_INDEX_S2": "STRESS_INDEX_S2",
            "STRESS_INDEX_S3": "STRESS_INDEX_S3",
            "BVP_amplitude_BIOGRAPH_średnia_S1": "BVP_amplitude_BIOGRAPH_średnia_S1",
            "BVP_amplitude_BIOGRAPH_średnia_S2": "BVP_amplitude_BIOGRAPH_średnia_S2",
            "BVP_amplitude_BIOGRAPH_średnia_S3": "BVP_amplitude_BIOGRAPH_średnia_S3",
            "TEMP_średnia_surowy_S1": "TEMP_średnia_surowy_S1",
            "TEMP_średnia_surowy_S2": "TEMP_średnia_surowy_S2",
            "TEMP_średnia_surowy_S3": "TEMP_średnia_surowy_S3",
            "TEM_BIOGRAPH_średnia_S1": "TEM_BIOGRAPH_średnia_S1",
            "TEM_BIOGRAPH_średnia_S2": "TEM_BIOGRAPH_średnia_S2",
            "TEM_BIOGRAPH_średnia_S3": "TEM_BIOGRAPH_średnia_S3",
            "GSR_średnia_surowy_S1": "GSR_średnia_surowy_S1",
            "GSR_średnia_surowy_S2": "GSR_średnia_surowy_S2",
            "GSR_średnia_surowy_S3": "GSR_średnia_surowy_S3",
            "GSR_BIOGRAPH_średnia_S1": "GSR_BIOGRAPH_średnia_S1",
            "GSR_BIOGRAPH_średnia_S2": "GSR_BIOGRAPH_średnia_S2",
            "GSR_BIOGRAPH_średnia_S3": "GSR_BIOGRAPH_średnia_S3",
            "RESP_średnia_surowy_S1": "RESP_średnia_surowy_S1",
            "RESP_średnia_surowy_S2": "RESP_średnia_surowy_S2",
            "RESP_średnia_surowy_S3": "RESP_średnia_surowy_S3",
            "RESP_BIOGRAPH_średnia_S1": "RESP_BIOGRAPH_średnia_S1",
            "RESP_BIOGRAPH_średnia_S2": "RESP_BIOGRAPH_średnia_S2",
            "RESP_BIOGRAPH_średnia_S3": "RESP_BIOGRAPH_średnia_S3",
            "RESP_NEUROKIT_średnia_S1": "RESP_NEUROKIT_średnia_S1",
            "RESP_NEUROKIT_średnia_S2": "RESP_NEUROKIT_średnia_S2",
            "RESP_NEUROKIT_średnia_S3": "RESP_NEUROKIT_średnia_S3",
            "Abd_amplitude_BIOGRAPH_średnia_S1": "Abd_amplitude_BIOGRAPH_średnia_S1",
            "Abd_amplitude_BIOGRAPH_średnia_S2": "Abd_amplitude_BIOGRAPH_średnia_S2",
            "Abd_amplitude_BIOGRAPH_średnia_S3": "Abd_amplitude_BIOGRAPH_średnia_S3",
            "Uwagi": "Uwagi",
            "Nazwa pliku BioGraph": "Nazwa pliku BioGraph",
            "PNS_index_S1": "PNS_index_S1",
            "PNS_index_S2": "PNS_index_S2",
            "PNS_index_S3": "PNS_index_S3",
            "SNS_index_S1": "SNS_index_S1",
            "SNS_index_S2": "SNS_index_S2",
            "SNS_index_S3": "SNS_index_S3",
            "Stress_index_S1": "Stress_index_S1",
            "Stress_index_S2": "Stress_index_S2",
            "Stress_index_S3": "Stress_index_S3",
            "Mean_RR_S1": "Mean_RR_S1",
            "Mean_RR_S2": "Mean_RR_S2",
            "Mean_RR_S3": "Mean_RR_S3",
            "SDNN_(ms)_S1": "SDNN_(ms)_S1",
            "SDNN_(ms)_S2": "SDNN_(ms)_S2",
            "SDNN_(ms)_S3": "SDNN_(ms)_S3",
            "Mean_HR_(beats/min)_S1": "Mean_HR_(beats/min)_S1",
            "Mean_HR_(beats/min)_S2": "Mean_HR_(beats/min)_S2",
            "Mean_HR_(beats/min)_S3": "Mean_HR_(beats/min)_S3",
            "SD_HR_(beats/min)_S1": "SD_HR_(beats/min)_S1",
            "SD_HR_(beats/min)_S2": "SD_HR_(beats/min)_S2",
            "SD_HR_(beats/min)_S3": "SD_HR_(beats/min)_S3",
            "Min_HR_(beats/min)_S1": "Min_HR_(beats/min)_S1",
            "Min_HR_(beats/min)_S2": "Min_HR_(beats/min)_S2",
            "Min_HR_(beats/min)_S3": "Min_HR_(beats/min)_S3",
            "Max_HR_(beats/min)_S1": "Max_HR_(beats/min)_S1",
            "Max_HR_(beats/min)_S2": "Max_HR_(beats/min)_S2",
            "Max_HR_(beats/min)_S3": "Max_HR_(beats/min)_S3",
            "RMSSD_(ms)_S1": "RMSSD_(ms)_S1",
            "RMSSD_(ms)_S2": "RMSSD_(ms)_S2",
            "RMSSD_(ms)_S3": "RMSSD_(ms)_S3",
            "NNxx_(beats)_S1": "NNxx_(beats)_S1",
            "NNxx_(beats)_S2": "NNxx_(beats)_S2",
            "NNxx_(beats)_S3": "NNxx_(beats)_S3",
            "pNNxx_(%)_S1": "pNNxx_(%)_S1",
            "pNNxx_(%)_S2": "pNNxx_(%)_S2",
            "pNNxx_(%)_S3": "pNNxx_(%)_S3",
            "SDANN_(ms)_S1": "SDANN_(ms)_S1",
            "SDANN_(ms)_S2": "SDANN_(ms)_S2",
            "SDANN_(ms)_S3": "SDANN_(ms)_S3",
            "SDNN_index_(ms)_S1": "SDNN_index_(ms)_S1",
            "SDNN_index_(ms)_S2": "SDNN_index_(ms)_S2",
            "SDNN_index_(ms)_S3": "SDNN_index_(ms)_S3",
            "LF/HF_ratio_FFT_spectrum_S1": "LF/HF_ratio_FFT_spectrum_S1",
            "LF/HF_ratio_FFT_spectrum_S2": "LF/HF_ratio_FFT_spectrum_S2",
            "LF/HF_ratio_FFT_spectrum_S3": "LF/HF_ratio_FFT_spectrum_S3",
            "LF/HF_ratio_AR_spectrum_S1": "LF/HF_ratio_AR_spectrum_S1",
            "LF/HF_ratio_AR_spectrum_S2": "LF/HF_ratio_AR_spectrum_S2",
            "LF/HF_ratio_AR_spectrum_S3": "LF/HF_ratio_AR_spectrum_S3",
            "RR_tri_index_S1": "RR_tri_index_S1",
            "RR tri index_S2": "RR tri index_S2",
            "RR tri index_S3": "RR tri index_S3",
            "TINN_(ms)_S1": "TINN_(ms)_S1",
            "TINN_(ms)_S2": "TINN_(ms)_S2",
            "TINN_(ms)_S3": "TINN_(ms)_S3",
            "SD1_(ms)_S1": "SD1_(ms)_S1",
            "SD1_(ms)_S2": "SD1_(ms)_S2",
            "SD1_(ms)_S3": "SD1_(ms)_S3",
            "SD2_(ms)_S1": "SD2_(ms)_S1",
            "SD2_(ms)_S2": "SD2_(ms)_S2",
            "SD2_(ms)_S3": "SD2_(ms)_S3",
            "SD2/SD1_S1": "SD2/SD1_S1",
            "SD2/SD1_S2": "SD2/SD1_S2",
            "SD2/SD1_S3": "SD2/SD1_S3",
            "Approximate_entropy_(ApEn)_S1": "Approximate_entropy_(ApEn)_S1",
            "Approximate_entropy_(ApEn)_S2": "Approximate_entropy_(ApEn)_S2",
            "Approximate_entropy_(ApEn)_S3": "Approximate_entropy_(ApEn)_S3",
            "Sample_entropy_(SampEn)_S1": "Sample_entropy_(SampEn)_S1",
            "Sample_entropy_(SampEn)_S2": "Sample_entropy_(SampEn)_S2",
            "Sample_entropy_(SampEn)_S3": "Sample_entropy_(SampEn)_S3",
            "alpha 1_S1": "alpha 1_S1",
            "alpha 1_S2": "alpha 1_S2",
            "alpha 1_S3": "alpha 1_S3",
            "alpha_2_S1": "alpha_2_S1",
            "alpha_2_S2": "alpha_2_S2",
            "alpha_2_S3": "alpha_2_S3"
        }     
    }
}

FIELD_TYPES = {
    "id": {
        "meta": {
            "value": str
        }
    },

    "dane": {
        "raw":{
            "Sygnatura czasowa": datetime,
            "Kod badanego 2": str,
            "Płeć": str,
            "Data urodzenia": datetime,
            "Status HL": str,
            "Status ET": str,
            "Status testów poznawczych": str,
            "Status biometrii": str,
            "Miejsce badania": str
        },
        "summary":{
            "Wiek": float,
            "Dni badanego": float,
            "Minuty trwania lekcji": int
        }
    },

    "zmęczenie":{
        "raw":{
            "NASA TLX MentalDemand": int,
            "NASA TLX PhysicalDemand": int,
            "NASA TLX TemporalDemand": int,
            "NASA TLX Performance": int,
            "NASA TLX Effort": int,
            "NASA TLX Frustration": int,
            "NASA TLX CalculatedTiredness": float
        },
        "summary":{
            "Różnica sakkad": float,
            "Różnica trwania fiksacji": float, 
            "Różnica długości sakkady": float,
            "Różnica testów PVT": float,
            "Różnica testów 2-back": float,
            "Różnica błędów 2-back": float,
            "Różnica braku reakcji 2-back": float,
            "Fatigue_ICA": float,
            "Q1+Q2/Q3+Q4_diff": float,
            "Q1/Q4_diff": float
        }
    },

    "pvt": {
        "raw":{
            "PVT kod badanego": str
        },
        "summary":{
            "Średnie PVT przed": float,
            "SD PVT przed": float,
            "Średnie PVT po": float,
            "SD PVT po": float,
            "Odfiltrowane >700ms": bool
        }
    },

    "tlx": {
        "raw":{
            "NASA TLX kod badanego": str,
            "NASA TLX MentalDemand": int,
            "NASA TLX PhysicalDemand": int,
            "NASA TLX TemporalDemand": int,
            "NASA TLX Performance": int,
            "NASA TLX Effort": int,
            "NASA TLX Frustration": int,
            "NASA TLX CalculatedTiredness": float
        }
    },

    "2-back":{
        "raw":{
            "2-back kod badanego": str,
            "2-back1 Liczba rekordów": int,
            "2-back1 Liczba sytuacji": int,
            "2-back1 Liczba poprawnych kliknięć": int,
            "2-back1 Liczba niepoprawnych kliknięć": int,
            "2-back1 Liczba niepoprawnych braków kliknięć": int,
            "2-back1 Liczba poprawnych braków kliknięć": int,
            "2-back2 Liczba rekordów": int,
            "2-back2 Liczba sytuacji": int,
            "2-back2 Liczba poprawnych kliknięć": int,
            "2-back2 Liczba niepoprawnych kliknięć": int,
            "2-back2 Liczba niepoprawnych braków kliknięć": int,
            "2-back2 Liczba poprawnych braków kliknięć": int
        },
        "summary":{
            "2-back1 Procent poprawnych kliknięć": float,
            "2-back1 Średnia czasów reakcji poprawnych kliknięć": float,
            "2-back1 Średnia czasów reakcji niepoprawnych kliknięć": float,
            "2-back2 Procent poprawnych kliknięć": float,
            "2-back2 Średnia czasów reakcji poprawnych kliknięć": float,
            "2-back2 Średnia czasów reakcji niepoprawnych kliknięć": float
        }
    },

    "doświadczenie":{
        "raw":{
            "Nauka zdalna": bool,
            "Nauka zdalna stres": int,
            "Doświadczenie VR": int,
            "Doświadczenie AR": int,
            "Przedział godzinowy": int
        }
    },

    "eas-d ws":{
        "summary":{
            "EAS-D WS Niezadowolenie": int,
            "EAS-D WS Strach": int,
            "EAS-D WS Złość": int,
            "EAS-D WS Aktywność": int,
            "EAS-D WS Towarzyskość": int
        }
    },

    "stai x1":{
        "summary":{
            "STAI X1 Lęk jako cecha1": int,
            "STAI X1 Lęk jako cecha2": int
        }
    },

    "quiz":{
        "raw":{
            "Quiz 1": bool,
            "Quiz 2": bool,
            "Quiz 3": bool,
            "Quiz 4": bool,
            "Quiz 5": bool
        },
        "summary":{
            "Quiz wynik": int
        }
    },

    "tam":{
        "summary":{
            "TAM IS": float,
            "TAM IS%": float,
            "TAM PU": float,
            "TAM PU%": float,
            "TAM PEU": float,
            "TAM PEU%": float,
            "TAM PE": float,
            "TAM PE%": float,
            "TAM ATU": float,
            "TAM ATU%": float,
            "TAM ITU": float,
            "TAM ITU%": float
        }
    },

    "ueq":{
        "summary":{
            "UEQ Atrakcyjność": float,
            "UEQ Przejrzystość": float,
            "UEQ Efektywność": float,
            "UEQ Zależność": float,
            "UEQ Poziom stymulacji": float,
            "UEQ Oryginalność": float
        }
    },

    "et": {
        "raw": {
            "ET kod Badanego": str,
            "AvatarChatGPTMrtkCanvas Total Time": float,
            "AvatarChatGPTMrtkCanvas Average Gaze Time": float,
            "BottomMoveHandle Total Time": float,
            "BottomMoveHandle Average Gaze Time": float,
            "CanvasButtonToggleSwitch Variant Total Time": float,
            "CanvasButtonToggleSwitch Variant Average Gaze Time": float,
            "CanvasButtonToggleSwitch Variant (1) Total Time": float,
            "CanvasButtonToggleSwitch Variant (1) Average Gaze Time": float,
            "CanvasButtonToggleSwitch Variant (2) Total Time": float,
            "CanvasButtonToggleSwitch Variant (2) Average Gaze Time": float,
            "CanvasButtonToggleSwitch Variant (3) Total Time": float,
            "CanvasButtonToggleSwitch Variant (3) Average Gaze Time": float,
            "EraserBigBoxToggle Total Time": float,
            "EraserBigBoxToggle Average Gaze Time": float,
            "FemaleAvatar_Animation_FakeLipSync Total Time": float,
            "FemaleAvatar_Animation_FakeLipSync Average Gaze Time": float,
            "Handle Total Time": float,
            "Handle Average Gaze Time": float,
            "MrtkButton Total Time": float,
            "MrtkButton Average Gaze Time": float,
            "NextButton Total Time": float,
            "NextButton Average Gaze Time": float,
            "PenBoxToggle Total Time": float,
            "PenBoxToggle Average Gaze Time": float,
            "Pendulum Total Time": float,
            "Pendulum Average Gaze Time": float,
            "PendulumPropertiesCanvas Total Time": float,
            "PendulumPropertiesCanvas Average Gaze Time": float,
            "PressableButton_32x32mm_IconAndText Total Time": float,
            "PressableButton_32x32mm_IconAndText Average Gaze Time": float,
            "PrevButton Total Time": float,
            "PrevButton Average Gaze Time": float,
            "RedoButton Total Time": float,
            "RedoButton Average Gaze Time": float,
            "RotateHandle (2) Total Time": float,
            "RotateHandle (2) Average Gaze Time": float,
            "RotateHandle (3) Total Time": float,
            "RotateHandle (3) Average Gaze Time": float,
            "ScaleHandle Total Time": float,
            "ScaleHandle Average Gaze Time": float,
            "SliderTrack Total Time": float,
            "SliderTrack Average Gaze Time": float,
            "TopMoveHandle Total Time": float,
            "TopMoveHandle Average Gaze Time": float,
            "Tray Total Time": float,
            "Tray Average Gaze Time": float,
            "UndoButton Total Time": float,
            "UndoButton Average Gaze Time": float,
            "WhiteboardCollider Total Time": float,
            "WhiteboardCollider Average Gaze Time": float
        }
    },

    "_external": {
        "raw": {
            "KES": bool,
            "czy były szczególne sytuacje": str,
            "STRESS_INDEX_S1": float,
            "STRESS_INDEX_S2": float,
            "STRESS_INDEX_S3": float,
            "BVP_amplitude_BIOGRAPH_średnia_S1": float,
            "BVP_amplitude_BIOGRAPH_średnia_S2": float,
            "BVP_amplitude_BIOGRAPH_średnia_S3": float,
            "TEMP_średnia_surowy_S1": float,
            "TEMP_średnia_surowy_S2": float,
            "TEMP_średnia_surowy_S3": float,
            "TEM_BIOGRAPH_średnia_S1": float,
            "TEM_BIOGRAPH_średnia_S2": float,
            "TEM_BIOGRAPH_średnia_S3": float,
            "GSR_średnia_surowy_S1": float,
            "GSR_średnia_surowy_S2": float,
            "GSR_średnia_surowy_S3": float,
            "GSR_BIOGRAPH_średnia_S1": float,
            "GSR_BIOGRAPH_średnia_S2": float,
            "GSR_BIOGRAPH_średnia_S3": float,
            "RESP_średnia_surowy_S1": float,
            "RESP_średnia_surowy_S2": float,
            "RESP_średnia_surowy_S3": float,
            "RESP_BIOGRAPH_średnia_S1": float,
            "RESP_BIOGRAPH_średnia_S2": float,
            "RESP_BIOGRAPH_średnia_S3": float,
            "RESP_NEUROKIT_średnia_S1": float,
            "RESP_NEUROKIT_średnia_S2": float,
            "RESP_NEUROKIT_średnia_S3": float,
            "Abd_amplitude_BIOGRAPH_średnia_S1": float,
            "Abd_amplitude_BIOGRAPH_średnia_S2": float,
            "Abd_amplitude_BIOGRAPH_średnia_S3": float,
            "Uwagi": str,
            "Nazwa pliku BioGraph": str,
            "PNS_index_S1": float,
            "PNS_index_S2": float,
            "PNS_index_S3": float,
            "SNS_index_S1": float,
            "SNS_index_S2": float,
            "SNS_index_S3": float,
            "Stress_index_S1": float,
            "Stress_index_S2": float,
            "Stress_index_S3": float,
            "Mean_RR_S1": float,
            "Mean_RR_S2": float,
            "Mean_RR_S3": float,
            "SDNN_(ms)_S1": float,
            "SDNN_(ms)_S2": float,
            "SDNN_(ms)_S3": float,
            "Mean_HR_(beats/min)_S1": float,
            "Mean_HR_(beats/min)_S2": float,
            "Mean_HR_(beats/min)_S3": float,
            "SD_HR_(beats/min)_S1": float,
            "SD_HR_(beats/min)_S2": float,
            "SD_HR_(beats/min)_S3": float,
            "Min_HR_(beats/min)_S1": float,
            "Min_HR_(beats/min)_S2": float,
            "Min_HR_(beats/min)_S3": float,
            "Max_HR_(beats/min)_S1": float,
            "Max_HR_(beats/min)_S2": float,
            "Max_HR_(beats/min)_S3": float,
            "RMSSD_(ms)_S1": float,
            "RMSSD_(ms)_S2": float,
            "RMSSD_(ms)_S3": float,
            "NNxx_(beats)_S1": float,
            "NNxx_(beats)_S2": float,
            "NNxx_(beats)_S3": float,
            "pNNxx_(%)_S1": float,
            "pNNxx_(%)_S2": float,
            "pNNxx_(%)_S3": float,
            "SDANN_(ms)_S1": float,
            "SDANN_(ms)_S2": float,
            "SDANN_(ms)_S3": float,
            "SDNN_index_(ms)_S1": float,
            "SDNN_index_(ms)_S2": float,
            "SDNN_index_(ms)_S3": float,
            "LF/HF_ratio_FFT_spectrum_S1": float,
            "LF/HF_ratio_FFT_spectrum_S2": float,
            "LF/HF_ratio_FFT_spectrum_S3": float,
            "LF/HF_ratio_AR_spectrum_S1": float,
            "LF/HF_ratio_AR_spectrum_S2": float,
            "LF/HF_ratio_AR_spectrum_S3": float,
            "RR_tri_index_S1": float,
            "RR tri index_S2": float,
            "RR tri index_S3": float,
            "TINN_(ms)_S1": float,
            "TINN_(ms)_S2": float,
            "TINN_(ms)_S3": float,
            "SD1_(ms)_S1": float,
            "SD1_(ms)_S2": float,
            "SD1_(ms)_S3": float,
            "SD2_(ms)_S1": float,
            "SD2_(ms)_S2": float,
            "SD2_(ms)_S3": float,
            "SD2/SD1_S1": float,
            "SD2/SD1_S2": float,
            "SD2/SD1_S3": float,
            "Approximate_entropy_(ApEn)_S1": float,
            "Approximate_entropy_(ApEn)_S2": float,
            "Approximate_entropy_(ApEn)_S3": float,
            "Sample_entropy_(SampEn)_S1": float,
            "Sample_entropy_(SampEn)_S2": float,
            "Sample_entropy_(SampEn)_S3": float,
            "alpha 1_S1": float,
            "alpha 1_S2": float,
            "alpha 1_S3": float,
            "alpha_2_S1": float,
            "alpha_2_S2": float,
            "alpha_2_S3": float
        }
    }
}

STUDY_META = {
    "version": "v1.0",
    "imported_by": "bartus"
}

def splaszczTypy(slownik: dict, prefix: str = "") -> dict:
    wynik = {}
    for k, v in slownik.items():
        path = f"{prefix}.{k}" if prefix else k
        if isinstance(v, dict):
            wynik.update(splaszczTypy(v, path))
        else:
            wynik[path] = v
    return wynik

FLAT_FIELD_TYPES = splaszczTypy(FIELD_TYPES)