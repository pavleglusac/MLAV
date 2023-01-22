import torchaudio
import torch
from voice_recognizer.mic import record

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

labels = [
	'backward',
	'down',
	'forward',
	'go',
	'left',
	'off',
	'on',
	'right',
	'stop',
	'up'
]

def get_likely_index(tensor):
	return tensor.argmax(dim=-1)

def label_to_index(word):
	return torch.tensor(labels.index(word))

def index_to_label(index):
	return labels[index]

def predict(tensor, model, transform):
	# tensor = tensor.to(device)
	tensor = transform(tensor)
	tensor = model(tensor.unsqueeze(0))
	tensor = get_likely_index(tensor)
	tensor = index_to_label(tensor.squeeze())
	return tensor

def load_waveform(path: str, exp_sample_rate: int):
	waveform, sample_rate = torchaudio.load(path)
	if exp_sample_rate != sample_rate:
		raise ValueError(f"sample rate should be {exp_sample_rate}, but got {sample_rate}")
	return waveform

class VoiceRecognizer:
	def __init__(self):
		self.model = torch.jit.load("voice_recognizer/voice_recognizer.pt")
		self.model.eval()
		# self.model = self.model.to(device)
		self.transform = torchaudio.transforms.Resample(orig_freq=16_000, new_freq=8_000)

	def record_and_predict(self):
		record()
		wave = load_waveform("output.wav", 16_000)
		return predict(wave, self.model, self.transform)